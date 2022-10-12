from itertools import count
import time
from playsound import playsound 
seconds = input("Digite o tempo em segundos: ")

def countDownTimer(seconds):
    
    while seconds > 0 :
        min = int(seconds/60)
        sec = int(seconds%60)
        if(sec<10):
            timer = f'{min}:0{sec}'
        else: 
            timer = f'{min}:{sec}' 
        print(timer,end="\r")
        time.sleep(1)
        seconds-=1 
    print('\033[1;35;46m⏱  \033[m' * 34)
    print('\033[1;31;46m{}Tempo Acabou{}\033[m'.format('  ' * 23, '  ' * 22))
    print('\033[1;35;46m⏱  \033[m' * 34)
    #playsound("mixkit-sound.wav")
    
countDownTimer(int(seconds))

