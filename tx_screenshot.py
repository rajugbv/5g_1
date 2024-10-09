import zmq
import cv2
import time
import numpy as np
import pyautogui


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:6666")

# Set the desired resolution (480p)
width, height = 480, 360

#cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
  #  time.sleep(1)
    #ret, frame = cap.read()
    frame = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

    #if not ret or frame is None:
    #    print("Error: Couldn't read frame from the camera.")
    #    break

    #frame = cv2.resize(frame, (640, 480))
    frame = cv2.resize(frame, (480, 360))
    encoded_frame, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = buffer.tobytes()

    socket.send(jpg_as_text)

    cv2.imshow("Webcam Stream", frame)

    if cv2.waitKey(1500) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

