import zmq
import cv2
import numpy as np

# Set up a ZMQ context and subscriber socket
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:6666")

# Subscribe to all messages
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    # Receive the image data from the publisher
    jpg_as_text = socket.recv()

    # Decode the received image data
    np_img = np.frombuffer(jpg_as_text, dtype=np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Display the received frame
    if frame is not None:
        cv2.imshow("Received Stream", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

