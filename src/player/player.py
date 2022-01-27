import vlc
import time
import os

mapping = {
    '1': './media/1.mp4',
    '2': './media/2.png',
}

def loop():
    vlc_instance = vlc.get_default_instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(mapping['1'])
    print(media)
    player.set_media(media)
    player.play()

loop()
time.sleep(100000);