import os

# path = '\\home\\wangles'
arquivos = os.listdir(path='/home/wangles/Documentos/Python')

for nome in arquivos:
    if '.py' in nome:
        print(nome)