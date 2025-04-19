
#aqui tengo una pregunta Boleana y una captura de valores 

#import re

#name = input("What's your name?").strip()
#matches = re.search(r"^(.+), ?(.+)$", name)#verificando si el patron ingresado en name es correcto y estan entre (.+),lo que estoy haciendo es capturando los valores por eso uso los (..)
#if matches:
#    name = matches.group(2) + " " + matches.group(1)#aqui estamos concatenando los dos en la variable sangrada name que no la usare
#print(f"Hello, {name}")

# el operador morza o walrus :=, permite asignar un valor y hacer una pregunta boleana,if ,elif

import re

name = input("What's your name?").strip()
if matches := re.search(r"^(.+), ?(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")