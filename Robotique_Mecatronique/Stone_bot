# Code qui permet de d'ouvrir un flux video , de calculer la distance entre le pouce et l'index
# de la main et de convertir cette distance en angle entre 0 et 180 degres pour faire tourner un
# servomoteur

import cv2
import mediapipe as mp
import math
import numpy as np
from pyfirmata2 import Arduino
import time

PORT = 'COM3'  # Il faut connecter la carte Arduino au COM 3 si c'est n'ai pas possible il faut
# changer la valeur de port
board = Arduino(PORT)
time.sleep(2)

servo_pin = board.get_pin('d:9:s')  # connecter le servomoteur a la broche 9 du Arduino

mp_hands =mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
time.sleep(1)

# distance min/max
DIST_MIN = 30
DIST_MAX = 200

def map_angle(distance):
    distance = np.clip(distance, DIST_MIN, DIST_MAX)
    angle = np.interp(distance, [DIST_MIN, DIST_MAX], [10, 170])
    return int(angle)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            h, w, _ = frame.shape

            # Pouce
            thumb = hand.landmark[4]
            x1, y1 = int(thumb.x * w), int(thumb.y * h)

            # Index
            index = hand.landmark[8]
            x2, y2 = int(index.x * w), int(index.y * h)

            # Distance
            distance = math.hypot(x2 - x1, y2 - y1)

            # Conversion distance en angle
            angle = map_angle(distance)

            # Envoi au servo
            servo_pin.write(angle)
            time.sleep(0.02)

            # Affichage
            cv2.circle(frame, (x1, y1), 8, (0, 255, 0), -1)
            cv2.circle(frame, (x2, y2), 8, (0, 255, 0), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

            cv2.putText(frame, f"Angle: {angle} deg",
                        (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2)

    cv2.imshow("Controle Servo - Main", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC pour quitter
        break

cap.release()
cv2.destroyAllWindows()
board.exit()