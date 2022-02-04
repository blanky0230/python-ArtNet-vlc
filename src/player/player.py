import vlc
import time
import glob
import os

from dotenv import load_dotenv
config = load_dotenv(".env") 

MEDIA_DIR=os.environ['MEDIA_DIR']

class VlcPlayer():

    def __init__(self):
        self.vlc_instance = vlc.get_default_instance()
        self.player = self.vlc_instance.media_player_new()
        self.player.set_fullscreen(True)
        self.player.audio_set_mute(True)
        self.video_id = -1
        self.folder_id = -1
        self.last_command = 0
        self.speed = 1
        self.catalogue = {}
        vlc.libvlc_media_player_set_rate(self.player, self.speed)

        folders=len(glob.glob(os.path.join(MEDIA_DIR, '*')))
        for i in range(folders):
            self.catalogue[i] = glob.glob(os.path.join(MEDIA_DIR, str(i), '*'))
            self.catalogue[i].sort()

        print("MEDIA CATALOGUE: {}".format(self.catalogue))


    def update(self, folder, media_id, command, speed):

        if folder > len(self.catalogue.keys()) or folder < 0:
            print("IMPOSSIBLE FOLDER, IGNORING UPDATE")
        

        if (media_id > len(self.catalogue[folder]) or media_id < 0):
            print("IMPOSSIBLE MEDIA ID, IGNORING UPDATE")
            return

        if not folder == self.folder_id or not media_id == self.video_id:
            media = self.vlc_instance.media_new(self.catalogue[folder][media_id])

            self.player.set_media(media)
            self.folder_id = folder
            self.video_id = media_id

            if command == 1:
                self.player.play()

        if command == 0:
            return

        elif command == 1:

            if self.last_command == 2:
                self.player.pause() #unpause if we were paused
            else:
                self.player.play()

        elif command == 2:
            self.player.pause()

        elif command == 3:
            self.player.stop()
