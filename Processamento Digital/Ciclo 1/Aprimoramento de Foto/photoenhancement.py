import cv2
import numpy as np
import os

def processar_foto_perfil(caminho_foto, pasta_saida):
    # Carrega a imagem de perfil
    imagem = cv2.imread(caminho_foto)
    
    if imagem is None:
        print(f"Erro ao carregar a imagem: {caminho_foto}")
        return

    # Divide a imagem nos canais de cor
    azul, verde, vermelho = cv2.split(imagem)

    # Mescla os canais de volta para garantir que a imagem original está intacta
    imagem_mesclada = cv2.merge((azul, verde, vermelho))

    # Inverte os canais para um efeito artístico
    imagem_invertida = cv2.merge((vermelho, verde, azul))

    # Cria uma máscara preta (imagem vazia)
    blank = np.zeros(imagem.shape[:2], dtype='uint8')

    # Cria imagens que destacam um canal de cor específico
    canal_azul = cv2.merge([azul, blank, blank])
    canal_verde = cv2.merge([blank, verde, blank])
    canal_vermelho = cv2.merge([blank, blank, vermelho])

    # Salva as imagens processadas na pasta de saída
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    cv2.imwrite(os.path.join(pasta_saida, 'Perfil_Azul.png'), canal_azul)
    cv2.imwrite(os.path.join(pasta_saida, 'Perfil_Verde.png'), canal_verde)
    cv2.imwrite(os.path.join(pasta_saida, 'Perfil_Vermelho.png'), canal_vermelho)
    cv2.imwrite(os.path.join(pasta_saida, "Perfil_Mesclado.png"), imagem_mesclada)
    cv2.imwrite(os.path.join(pasta_saida, "Perfil_Invertido.png"), imagem_invertida)

# Exemplo de uso:
# Supondo que as fotos de perfil dos usuários estão armazenadas em uma pasta chamada 'fotos_perfil'
# E queremos salvar as versões processadas em uma pasta 'fotos_perfil_processadas'
caminho_foto = 'fotos_perfil/usuario1.png'  # Caminho da foto de perfil
pasta_saida = 'fotos_perfil_processadas'     # Pasta para salvar as imagens processadas
processar_foto_perfil(caminho_foto, pasta_saida)
