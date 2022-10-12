import os
import cv2


path = "C:/Users/MARCO ANTONIO/Documents/Python/Aula105/Images"

images = []



for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)


frame = cv2.imread(images[0])
h,w,channels = frame.shape
size = (w,h)
print(size)

video = cv2.VideoWriter("C:/Users/MARCO ANTONIO/Documents/Python/Aula105/aula105.mp4",
cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    video.write(frame)
video.realese()
print('concluido')    


