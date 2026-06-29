import cv2
import math
import cvzone
import numpy as np
from ultralytics import YOLO
from sort import *

# WEBCAM
cap = cv2.VideoCapture(0)

# LOAD YOLO MODEL
model = YOLO("yolov8n.pt")

# CLASS NAMES
classNames = []
with open("coco.txt", "r") as f:
    classNames = f.read().splitlines()

# TRACKER
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

while True:

    success, img = cap.read()

    if not success:
        break

    results = model(img, stream=True)

    detections = np.empty((0, 5))

    for r in results:
        boxes = r.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            conf = math.ceil((box.conf[0] * 100)) / 100

            if conf > 0.5:

                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))

    resultsTracker = tracker.update(detections)

    for result in resultsTracker:

        x1, y1, x2, y2, Id = result
        x1, y1, x2, y2, Id = int(x1), int(y1), int(x2), int(y2), int(Id)

        w, h = x2 - x1, y2 - y1

        cvzone.cornerRect(img, (x1, y1, w, h), l=9)

        cvzone.putTextRect(
            img,
            f'ID: {Id}',
            (max(0, x1), max(35, y1)),
            scale=2,
            thickness=2,
            offset=10
        )

    cv2.imshow("Object Detection and Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()