from stupidArtnet import StupidArtnetServer
import os,time

from dotenv import load_dotenv
config = load_dotenv(".env") 

UDP_IP=os.environ['UDP_IP']
UDP_PORT=os.environ['UDP_PORT']
UNIVERSE=int(os.environ['UNIVERSE'])
SUBNET=int(os.environ['SUBNET'])
NET=int(os.environ['NET'])

DEBUG=True

server = StupidArtnetServer()

universe_id = server.register_listener(
    UNIVERSE, SUBNET, NET, False)

print(server)

while True:
    buffer = bytes(server.get_buffer(universe_id))
    if len(buffer) == 512:
        print("VIDEO ID: ", buffer[NET-1] * 0x0001 + buffer[NET] * 0x0001)
        print("COMMAND: ", buffer[NET+1])
        print("PLAYBACK SPEED ???: ", buffer[NET+2] * 0x0001 + buffer[::NET+4] * 0x0001)
    time.sleep(0.5)
