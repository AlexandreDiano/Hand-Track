import cv2
import time
import HandTrackingModule as htm
import os

cap = cv2.VideoCapture(0)

# folderPath = 'FingerImages'
# myList = os.listdir(folderPath)
pTime = 0

detector = htm.handDtector(detectionCon=0.75)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
