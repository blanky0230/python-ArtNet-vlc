import socket, os

from dotenv import load_dotenv
config = load_dotenv(".env") 

UDP_IP=os.environ['UDP_IP']
UDP_PORT=os.environ['UDP_PORT']
UNIVERSE=int(os.environ['UNIVERSE'])
SUBNET=int(os.environ['SUBNET'])
CHANNEL=int(os.environ['CHANNEL'])

DEBUG=True

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((UDP_IP, int(UDP_PORT)))

def extract_command(msg):
    return [msg[i] for i in range(CHANNEL -1, CHANNEL +4)]


def should_handle(msg):
    return int(extract_universe(msg)) == UNIVERSE  and extract_subnet(msg) == SUBNET and msg[9] == 0x50

def extract_universe(msg):
    return msg[14]

def extract_subnet(msg):
    return msg[15]

def extract_dmx_channel(msg):
    return (msg[16] + msg[17]) * 0x01

def debug_message(msg):
    print("OP_CODE LOW: ", msg[8])
    print("OP_CODE HIGH: ", msg[9])
    print("ART_NET LOW: ", msg[10])
    print("ART_NET HIGH: ", msg[11])

    print("SQUENCE: ", msg[12])

    print("UNIVERSE: ", extract_universe(msg))
    print("SUBNET: ", extract_subnet(msg))
    print("DMX_CHANNEL: ", extract_dmx_channel(msg))


def handle_message():
    (data, addr) = socket.recvfrom(1024)
    if DEBUG:
        debug_message(data)


    if should_handle(data):
        command = extract_command(data)
        mediaId = sum(command[0::1])
        print("(I would select Media) MEDIA ID: ", mediaId)
        plabackSpeed = sum(command[3::5])
        print("(I would do 0 = nothing, 1 = play, 2 = pause, 3 = stop) OPCODE: ", command[2])
        print("(I dunno how'd interpret that but I guess set a percentage or something) PLAYBACK SPD: ", plabackSpeed)

        

while True:
    handle_message()
