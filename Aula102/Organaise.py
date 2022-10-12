from distutils import extension
import os 
import shutil

#diretório de origem
from_dir = "C:/Users/MARCO ANTONIO/Downloads/PRO_1-1_C102_AtividadeDoAluno1"
#diretório de destino
to_dir = "C:/Users/MARCO ANTONIO/Documents/Python/Aula102"
lista_de_arquivos = os.listdir(from_dir )
#print(lista_de_arquivos)

for arquivo in lista_de_arquivos:
    nome,extensao = os.path.splitext(arquivo)
    #print(nome)
    #print(extensao)
    if extensao == "":
        continue
    if extensao in [".gif",".png",".jpeg",".jpg",".jfif"]:
        pasta1 = from_dir+"/"+arquivo
        pasta2 = f'{to_dir}/imagens'
        pasta3 = f'{to_dir}/imagens/{arquivo}'
        
        #print(pasta1)
        #print(pasta3) 
        if os.path.exists(pasta2):
            print(f'movendo {arquivo}...')
            shutil.move(pasta1,pasta3)
        else:
            os.makedirs(pasta2)
            print(f'movendo {arquivo}...')
            shutil.move(pasta1,pasta3)     