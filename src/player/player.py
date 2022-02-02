import vlc
import time
import glob
class VlcPlayer():

    def __init__(self):
        self.vlc_instance = vlc.get_default_instance()
        self.player = self.vlc_instance.media_player_new()
        self.video_id = 0
        self.command = 0
        self.catalogue=glob.glob('./media/*')
        self.catalogue.sort()


    def update(self, media_id, command, extra):

        if (media_id > len(self.catalogue)):
            print("IMPOSSIBLE MEDIA ID, IGNORING UPDATE")
            return

        media = self.vlc_instance.media_new(self.catalogue[media_id -1])
        self.player.set_media(media)

        if command == 0:
            return
        elif command == 1:
            self.player.play()
        elif command == 2:
            self.player.pause()
        elif command == 3:
            self.player.stop()