import os 
import shutil
from xmlrpc.server import list_public_methods

from_dir = "C:/Users/MARCO ANTONIO/Downloads"

to_dir = "C:/Users/MARCO ANTONIO/Documents/Python/Projeto102/Arquivos_documentos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
    nome,extensao = os.path.splitext(file)
    if extensao == "":
        continue
    if extensao in [".txt", ".doc", ".docx", ".pdf",
                    ".gif",".png",".jpeg",".jpg",".jfif"]:
        path1 = from_dir+"/"+file
        path2 = f'{to_dir}/imagens'
        path3 = f'{to_dir}/imagens/{file}'
        
        if os.path.exists(path2):
            print(f'Movendo {file}...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print(f'Movendo {file}...')
            shutil.move(path1,path3)    