from stupidArtnet import StupidArtnetServer
from player import VlcPlayer
import os
import time
import tkinter as Tk
from tkinter import ttk

from dotenv import load_dotenv
config = load_dotenv(".env")

UDP_IP = os.environ['UDP_IP']
UDP_PORT = os.environ['UDP_PORT']
UNIVERSE = int(os.environ['UNIVERSE'])
SUBNET = int(os.environ['SUBNET'])
NET = int(os.environ['NET'])-1

DEBUG = True

server = StupidArtnetServer()

universe_id = server.register_listener(
    UNIVERSE, SUBNET, NET, False)

print(server)
old_state = {}
root = Tk.Tk()
root.attributes('-topmost', 1)
root.attributes('-fullscreen', True)
root.configure(bg='black')
player = VlcPlayer(root)


def update():
    root.update()
    global old_state
    try:
        buffer = bytes(server.get_buffer(universe_id))
        if len(buffer) == 512:
            new_state = {'folder': buffer[NET], 'media_id': buffer[NET+1],
                         'command': buffer[NET+2], 'speed': buffer[NET+3], 'logo': buffer[NET+4]}
            if (not old_state == new_state):
                print(new_state)
                player.update(**new_state)
                old_state = new_state
    except Exception as e:
        print("SOME ERROR OCCURED! Trying not to die...")
        print(str(e))
        raise e

while True:
    update()