import cv2
import numpy as np

img = cv2.imread("C:/Users/MARCO ANTONIO/Documents/Python/Projeto104/solar-system.jpg")

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            color=(3, 161, 252))
cv2.putText(img,
            "Mercurio",
            (120,190),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.6,
            color=(252, 227, 3))
cv2.putText(img,
            "Venus",
            (195,180),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.6,
            color=(252, 227, 3))
cv2.putText(img,
            "Terra",
            (285,175),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.6,
            color=(252, 227, 3))
cv2.putText(img,
            "Marte",
            (380,185),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.6,
            color=(252, 227, 3))
cv2.putText(img,
            "Jupiter",
            (500,70),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.8,
            color=(252, 227, 3))
cv2.putText(img,
            "Saturno",
            (760,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.8,
            color=(252, 227, 3))
cv2.putText(img,
            "Urano",
            (965,145),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            color=(252, 227, 3))
cv2.putText(img,
            "Netuno",
            (1110,155),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            color=(252, 227, 3))

  
cv2.imshow("Apresento",img)
cv2.waitKey(0)

