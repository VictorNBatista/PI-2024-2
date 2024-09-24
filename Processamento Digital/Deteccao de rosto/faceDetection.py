from PIL import Image, ImageDraw, ImageEnhance
from skimage import measure
import numpy as np
import cv2

def detectar_rosto_e_contorno(caminho_imagem, pasta_saida):
    # Carrega a imagem de perfil
    imagem = Image.open(caminho_imagem)
    
    # Converter para escala de cinza
    imagem_cinza = imagem.convert('L')
    
    # Converter para matriz numpy para facilitar o processamento
    matriz_imagem = np.array(imagem_cinza)

    # Carrega o classificador Haar Cascade para detecção de rosto
    detector_rosto = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detecta os rostos na imagem
    rostos = detector_rosto.detectMultiScale(matriz_imagem, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Caso encontre rostos, desenha contornos
    if len(rostos) > 0:
        desenhar = ImageDraw.Draw(imagem)
        for (x, y, w, h) in rostos:
            # Desenha o contorno ao redor do rosto
            desenhar.rectangle([x, y, x+w, y+h], outline="red", width=3)

    # Realça o contraste da imagem
    realcar = ImageEnhance.Contrast(imagem)
    imagem = realcar.enhance(2.0)

    # Salva a imagem com contornos na pasta de saída
    imagem.save(f'{pasta_saida}/perfil_rosto_contorno.jpg')

# Exemplo de uso:
# Supondo que as fotos de perfil estão armazenadas na pasta 'fotos_perfil'
caminho_imagem = 'fotos_perfil/usuario1.png'
pasta_saida = 'fotos_perfil_processadas'
detectar_rosto_e_contorno(caminho_imagem, pasta_saida)
