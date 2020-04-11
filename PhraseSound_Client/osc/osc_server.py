import argparse
import math

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer


def print_handler(address, *args):
    print(f"{address}: {args}")


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port", type=int, default=1337, help="The port to listen on")
args = parser.parse_args()

# create dispatcher
dispatcher = Dispatcher()
dispatcher.map("/distance", print_handler)
dispatcher.map("/trigger", print_handler)

# create server
server = BlockingOSCUDPServer((args.ip, args.port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()  # Blocks forever