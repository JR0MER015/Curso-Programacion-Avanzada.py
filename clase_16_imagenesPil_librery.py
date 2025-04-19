#biblioteca PILLOW que te permite usar archivos de imagenes

#crear un progrma que cree un gif animado 
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:#iterando sobre los argumetos,para que inicie desde 1
    image = Image.open(arg) #creo una variable y le doy la lista , y la libreria me dara funciones para usar con la imagen 
    images.append(image)
    
#aqui no se necesita abrir o cerrar el archivo , la libreria lo hace por nosotros

images[0].save(
    "costumes.gif",save_all= True, append_images = [images[1]],duration =200, loop= 0
)

#loop 0 significa que sera un bucle infinito
#dirección
#& C:/Users/jcrom/AppData/Local/Programs/Python/Python312/python.exe c:/Users/jcrom/Desktop/Python/curso_edutin_programacion_avanzada.py/clase_16_imagenesPil_librery.py costume1.gif costume2.gif

#C:\Users\jcrom\Desktop\Python\costumes.gif