import cv2
import numpy as np 

img = cv2.imread("C:/Users/MARCO ANTONIO/Documents/Python/Aula104/poster.jpg")

cv2.imshow("Janela 1",img)
 

rocket = img[120:360,400:500]
img[0:240,500:600] = rocket
texto = "Eu amo Programar"
cv2.putText(img,texto,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.6,color=(0,0,255)) 
cv2.imshow("janela 2",rocket)
cv2.imshow("Janela 1",img)
cv2.waitKey(0)

