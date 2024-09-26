# Processamento de Imagens no Projeto Learrny

Este repositório contém scripts em Python para realizar processamento de imagens de perfil e detecção facial na plataforma Learrny, além de funcionalidades para contagem de pixels e contorno em imagens. As tecnologias utilizadas incluem OpenCV, PIL (Pillow), Scikit-Image e NumPy.

## Instalação

### 1. Clone o repositório:
```bash
git clone https://github.com/VictorNBatista/PI-2024-2.git
```

### 2. Instale as dependências:

* opencv-python
```bash
pip install opencv-python
```

* Pillow
```bash
pip install pillow
```
* scikit-image
```bash
pip install scikit-image
```

* numpy
```bash
pip install numpy
```

## Funcionalidades
### Processamento de Imagens de Perfil
O script rgb.py processa as fotos de perfil dos usuários da plataforma Learrny. Ele realiza operações como:

* Separação dos canais de cor (vermelho, verde, azul).
* Criação de variações estilizadas da imagem de perfil.
* Realce automático da imagem.

As imagens processadas são salvas na pasta de saída especificada.

### Detecção de Rostos e Contorno
O script preprocessing.py detecta rostos em imagens utilizando o classificador Haar Cascade do OpenCV. Após detectar os rostos, ele desenha contornos ao redor deles e salva a imagem processada.

## Tecnologias Utilizadas
* Python: Linguagem de programação usada para implementar os scripts.
* OpenCV: Biblioteca utilizada para manipulação de imagens e detecção facial.
* Pillow (PIL): Biblioteca para carregar e desenhar em imagens.
* Scikit-Image: Usada para detecção de contornos.
* NumPy: Biblioteca para manipulação eficiente de arrays e matrizes de dados.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
