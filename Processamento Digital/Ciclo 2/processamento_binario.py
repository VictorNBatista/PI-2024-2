import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem em escala de cinza (necessário para o limiar)
img = cv2.imread("Aguia.jpeg", 0)

# Método 1: Limiarização com limiar fixo (opcional)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # Experimente o valor do limiar

# Método 2: Limiarização adaptativa (recomendado)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Transformações (Exemplo: rotação, translação e escala)
# Rotação de 45 graus
height, width = img.shape
M_rot = cv2.getRotationMatrix2D((width//2, height//2), 45, 1)  # Rotação de 45 graus
rotated_img = cv2.warpAffine(img, M_rot, (width, height))

# Translação
M_trans = np.float32([[1, 0, 50], [0, 1, 50]])  # Translação de 50px em x e y
translated_img = cv2.warpAffine(img, M_trans, (width, height))

# Escala (aumento de tamanho)
scaled_img = cv2.resize(img, (width*2, height*2))  # Redimensionar para o dobro do tamanho

# Realce de imagem (Exemplo: equalização de histograma)
equalized_img = cv2.equalizeHist(img)  # Equalização de histograma para melhorar o contraste

# Filtragem (Exemplo: filtro de suavização e detecção de bordas)
# Filtro de média (suavização)
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

# Detecção de bordas com o filtro Sobel
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)  # Magnitude das bordas

# Exibir imagens de resultados
plt.figure(figsize=(12, 12))

# Imagem binária
plt.subplot(3, 3, 1)
plt.imshow(thresh1, 'gray')
plt.title('Imagem Binária (Limiar Fixo)')

plt.subplot(3, 3, 2)
plt.imshow(thresh2, 'gray')
plt.title('Imagem Binária (Limiar Adaptativo)')

# Transformações
plt.subplot(3, 3, 3)
plt.imshow(rotated_img, 'gray')
plt.title('Imagem Rotacionada (45°)')

plt.subplot(3, 3, 4)
plt.imshow(translated_img, 'gray')
plt.title('Imagem Transladada')

plt.subplot(3, 3, 5)
plt.imshow(scaled_img, 'gray')
plt.title('Imagem Escalada')

# Realce
plt.subplot(3, 3, 6)
plt.imshow(equalized_img, 'gray')
plt.title('Imagem Equalizada')

# Filtragem
plt.subplot(3, 3, 7)
plt.imshow(blurred_img, 'gray')
plt.title('Imagem Suavizada (Filtro de Média)')

plt.subplot(3, 3, 8)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Bordas Detectadas (Filtro Sobel)')

plt.tight_layout()
plt.show()

# Considerações adicionais e tratamento de erros
try:
    if img is None:
        print("Erro: Imagem não foi carregada. Verifique o caminho e o formato do arquivo.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
