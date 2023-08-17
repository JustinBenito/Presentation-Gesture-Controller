# import cv2
# import pyautogui
# from cvzone.HandTrackingModule import HandDetector
# import time
# width, height = 1280, 720

# cam = cv2.VideoCapture(1)
# cam.set(3, width)
# cam.set(4, height)
# handdetector = HandDetector(detectionCon=0.8, maxHands=1)

# while True:
#     sucss, img = cam.read()
#     hands, img = handdetector.findHands(img)
#     if len(hands) > 0:
#         hand = hands[0]
#         fingers = handdetector.fingersUp(hand)
#         print(fingers)
#     if fingers == [0, 1, 0, 0, 0]:
#         print("Option 1")
#         #next slide
#         pyautogui.press('right')
#         time.sleep(2)
#     if fingers == [0, 1, 1, 0, 0]:
#         print("Option 2")
#         #previous slide
#         pyautogui.press('left')
#         time.sleep(2)
#     if fingers == [0, 1, 1, 1, 0]:
#         print("Option 3")
#         pyautogui.press('esc')
#         time.sleep(2)
#     if fingers == [0, 1, 1, 1, 1]:
#         print("Option 3")
#         pyautogui.press('q')
#         time.sleep(2)
#     cv2.imshow("Video", img)
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

import cv2
import mediapipe as mp
import pyautogui
import time

cam = cv2.VideoCapture(1)
cam.set(3, 1280)
cam.set(4, 720)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

while True:
    success, img = cam.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        fingers = [0, 0, 0, 0, 0]

        # Check which fingers are up
        if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
            fingers[1] = 1
        if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
            fingers[0] = 1
        if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
            fingers[2] = 1
        if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y:
            fingers[3] = 1
        if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y:
            fingers[4] = 1

        print(fingers)

        if fingers == [0, 1, 0, 0, 0]:
            print("Option 1")
            #pyautogui.press('right')
            # time.sleep(2)
        elif fingers == [0, 1, 1, 0, 0]:
            print("Option 2")
            #pyautogui.press('left')
            #time.sleep(2)
        elif fingers == [0, 1, 1, 1, 0]:
            print("Option 3")
            #pyautogui.press('esc')
            #time.sleep(2)
        elif fingers == [0, 1, 1, 1, 1]:
            print("Option 3")
            #pyautogui.press('q')
            #time.sleep(2)

    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
