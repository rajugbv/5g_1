import base64
import cv2
import zmq
import time
import argparse  # Import argparse module

# Setup command line argument parsing
parser = argparse.ArgumentParser(description='Stream with custom text.')
parser.add_argument('--new_text', type=str, help='Custom parameters to send', required=True)
args = parser.parse_args()

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
#HOST = "10.205.5.24"
HOST = "127.0.1.1"
PORT = 9990
footage_socket.connect(f"tcp://{HOST}:{PORT}")

num = 0
start = time.time()


#time.sleep(0.2)
time.sleep(1)
current_time = str(time.time())
# Use the new_text value from command line
text_to_send = args.new_text +"Helal"+current_time+"Helal"
footage_socket.send_string(text_to_send)
print(text_to_send)


