import datetime
import time

import cv2

capture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(capture.get(3)), int(capture.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

while True:
    _, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
    for(x, y, width, height) in bodies:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("Date-%m-%d-Time-%H-%M-%S")
            output = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 20, frame_size)
            print(f"Started Recording at {current_time}")
    elif detection:
        if timer_started:
            if (time.time() - detection_stopped_time) > SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                output.release()
                print(f"Stopped Recording at {current_time}")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        output.write(frame)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break
output.release()
capture.release()
cv2.destroyAllWindows()