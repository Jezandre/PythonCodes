""""
mover arquivos pelo Python
"""
import os
import shutil

caminho_original = r'C:\Users\jucel\Desktop\ar1'
caminho_novo = r'C:\Users\jucel\Desktop\ar2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'{caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.xls' in file:
            os.remove(new_file_path)

        print(new_file_path)

        # if '.xls' in file:
        #     shutil.copy(old_file_path, new_file_path)
        #     print(f'Arquivo {file} movido com sucesso!')
