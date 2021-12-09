from PIL import Image
import os

# listagem de imagens:
listagem = os.listdir('E:\Arquivos de Programas\Projetos\Scripts\Testes\Conversor de Imagens\imagens')

print(listagem)

for arquivo in listagem:
    # abrir arquivo
    imagem = Image.open(f'imagens/{arquivo}')

    # salvar o arquivo com outro formato
    imagem.save(f'tiff/{arquivo.replace("png", "tiff")}')
