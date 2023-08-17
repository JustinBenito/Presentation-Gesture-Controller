import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector
import time
width, height = 1280, 720


cam = cv2.VideoCapture(0)
cam.set(3, width)
cam.set(4, height)
handdetector = HandDetector(detectionCon=0.8, maxHands=1)


while True:
    sucss, img = cam.read()
    hands, img = handdetector.findHands(img)
    if len(hands) > 0:
        hand = hands[0]
        fingers = handdetector.fingersUp(hand)
        print(fingers)
    if fingers == [0, 1, 0, 0, 0]:
        print("Option 1")
        pyautogui.press('right')
        time.sleep(2)
    if fingers == [0, 1, 1, 0, 0]:
        print("Option 2")
        pyautogui.press('left')
        time.sleep(2)
    if fingers == [0, 1, 1, 1, 1]:
        print("Option 2")
        pyautogui.press('q')
        time.sleep(2)
    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
