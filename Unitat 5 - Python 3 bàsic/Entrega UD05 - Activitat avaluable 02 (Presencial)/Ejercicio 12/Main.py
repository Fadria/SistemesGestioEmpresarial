from PIL import Image # Librería que nos permite procesar imágenes
import pytesseract # Librería para poder pasar una imagen a un String
from PIL import ImageEnhance # Añadimos una mayor capacidad de reconocimiento de texto

# Indicamos la ruta a nuestra instalación de tesseract. En Windows lo instalamos con el .exe de este directorio
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\fadri\Documents\Librerias\Tesseract\tesseract'

img = Image.open('imagenTexto.png') # Abrimos la imagen localizada en este directorio

# Mejoramos la nitidez y el contraste de la imagen
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)

# Guardamos la nueva imagen
img_edit.save("edited_image.png")

result = pytesseract.image_to_string(img_edit) # Convertimos la imagen modificada a String y la guardamos en la variable

print("El texto encontrado en la imagen es el siguiente:")
print(result) # Mostramos el texto encontrado en la imagen