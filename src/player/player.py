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
        self.video_id = 0
        self.last_command = 0
        self.speed = 1
        vlc.libvlc_media_player_set_rate(self.player, self.speed)
        self.catalogue=glob.glob(os.path.join(MEDIA_DIR, '*'))
        self.catalogue.sort()


    def update(self, media_id, command, extra):
        if (media_id > len(self.catalogue) or media_id < 0):
            print("IMPOSSIBLE MEDIA ID, IGNORING UPDATE")
            return

        if not media_id == self.video_id:
            media = self.vlc_instance.media_new(self.catalogue[media_id -1])
            self.player.set_media(media)
            self.video_id = media_id

        if not command == self.last_command:
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

        self.last_command = command