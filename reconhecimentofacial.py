import cv2
from deepface import DeepFace

# Ler a Imagem
imagem = cv2.imread("img2.jpg")

# Passar a imagem para a DeepFace
resultado = DeepFace.analyze(imagem, actions=("age", "emotion"))

# Ver os resultados da analise
print(resultado)