from distutils import extension
from fileinput import filename
import os 
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/MARCO ANTONIO/Downloads"
to_dir = "C:/Users/MARCO ANTONIO/Documents"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
       name,extension = os.path.splitext(event.src_path)
       
       for key,value in dir_tree.items():
           if extension in value:
               file_name = os.path.basename(event.src_path)
               path1 = from_dir+"/"+file_name
               path2 = to_dir+"/"+key
               path3 = to_dir+"/"+key+"/"+file_name
               time.sleep(3)
               if os.path.exists(to_dir+"/"+key):
                   if os.path.exists(path2):
                       print(f'Movendo {file_name}...')
                       shutil.move(path1,path3)
                   else:
                       os.makedirs(path2)
                       print(f'Movendo {file_name}...')
                       shutil.move(path1,path3)
                            
                 


gerenciador_evento = FileMovementHandler()
observador = Observer()
observador.schedule(gerenciador_evento,from_dir,recursive = True)
observador.start()

try:
    while True:
        time.sleep(2)
        print("executando")
except KeyboardInterrupt:
    print("interrompido")
    observador.stop()            
