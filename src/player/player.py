import vlc
import time
import glob
import os

from dotenv import load_dotenv
config = load_dotenv(".env")
import tkinter as Tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

MEDIA_DIR = os.environ['MEDIA_DIR']


class VlcPlayer(Tk.Frame):

    def __init__(self, parent, title=None):
        Tk.Frame.__init__(self,parent,  borderwidth=0)
        
        self.parent = parent
        self.videopanel = ttk.Frame(self.parent)

        self.canvas = Tk.Canvas(self.videopanel, background='black', highlightthickness=0)
        self.canvas.pack(fill=Tk.BOTH, expand=1)

        self.videopanel.pack(fill=Tk.BOTH, expand=1)
        self.parent.bind("<Configure>", self.OnConfigure)  # catch window resize, etc.

        self.vlcInstance = vlc.Instance('--video-wallpaper')
        self.player = self.vlcInstance.media_player_new()

        self.player.video_set_logo_int(
            vlc.VideoLogoOption.logo_opacity, 255)

        self.player.video_set_logo_int(
            vlc.VideoLogoOption.logo_position, 4)

        self.video_id = -1
        self.folder_id = -1
        self.last_command = 0
        self.speed = 1
        self.catalogue = {}
        self.windowHandle = self.videopanel.winfo_id()

        if os.name == 'nt':
            self.player.set_hwnd(self.windowHandle)

        elif os.name == 'posix':
            self.player.set_xwindow(self.windowHandle)

        else:
            pass #Screw MacOS nobody needs that :3


        vlc.libvlc_media_player_set_rate(self.player, self.speed)
        self.logos = glob.glob(os.path.join(MEDIA_DIR, 'logos', '*'))

        folders = len(glob.glob(os.path.join(MEDIA_DIR, '**')))
        for i in range(folders):
            self.catalogue[i] = glob.glob(os.path.join(MEDIA_DIR, str(i), '*'))
            self.catalogue[i].sort()

        print("LOGOS: {}".format(self.logos))
        print("MEDIA CATALOGUE: {}".format(self.catalogue))

    def OnConfigure(self, *unused):
        pass

    def OnClose(self, *unused):
        self.parent.quit()
        self.parent.destroy()

    def update(self, folder, media_id, command, speed, logo):
        if logo < 1:
            self.player.video_set_logo_int(vlc.VideoLogoOption.logo_enable, 0)
        else:
            if logo - 1 > len(self.logos):
                print("IMPOSSIBLE LOGO, IGNORING UPDATE")
                return
            self.player.video_set_logo_int(vlc.VideoLogoOption.logo_enable, 1)
            self.player.video_set_logo_string(
                vlc.VideoLogoOption.logo_file, self.logos[logo - 1])

        if folder > len(self.catalogue.keys()) or folder < 0:
            print("IMPOSSIBLE FOLDER, IGNORING UPDATE")
            return

        if media_id > len(self.catalogue[folder]) or media_id < 0:
            print("IMPOSSIBLE MEDIA ID, IGNORING UPDATE")
            return

        if speed < 10 or speed > 255:
            print("IMPOSSIBLE SPEED: '{}', IGNORING UPDATE".format(speed))
            return

        if not folder == self.folder_id or not media_id == self.video_id:
            media = self.vlcInstance.media_new_path(
                self.catalogue[folder][media_id])

            self.player.set_media(media)

            self.folder_id = folder
            self.video_id = media_id

            # if media is changed after pause - our pause-resume hack has to be reset
            self.last_command = -1

        if command == 0:
            return

        elif command == 1:

            if self.last_command == 2:
                self.player.pause()  # unpause if we were paused
            else:
                self.player.play()

        elif command == 2 and self.player.is_playing():
            self.player.pause()

        elif command == 3:
            self.player.stop()

        vlc.libvlc_media_player_set_rate(self.player, speed / 100)
        self.last_command = command
