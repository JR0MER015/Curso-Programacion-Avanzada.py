#estableciendo un formato para reformatear el formato que el usuario me de
#esto ayuda en caso de se ingrese los nombres asi Romero,Juan
#name = input("What's your name?").strip()
#if "," in name:
#    last, first = name.split(", ")#aqui tendo un espacio despues de la coma,pero esto podria ser opcional, por lo cual podemos usar caracter de una expresión regular
#    name = f"{first} {last}"
#print(f"Hello, {name}")

#el problema con este código es que se puede ingresar cualquier cosa antes de eso
#name = input("What's your name?").strip()
#if "," in name:
#    last, first = name.split(", ?")#aqui uso  ? que dice que la coma o el espacio son opcionales,el problema que esto no soporta expresiones regulares ,si quiero usar una expresión regular debo importar una libreria
#    name = f"{first} {last}"
#print(f"Hello, {name}")

#importo una libreria RE par el uso de expresiones regulares en conjunto con la funcion split
#recordando
#A|B = either A or B
#(...) = a group, capturing
#(?...) = non-capturing version


#import re

#name = input("What's your name?").strip()
#matches = re.search(r"^(.+),(.+)$", name)#verificando si el patron ingresado en name es correcto y estan entre (.+),lo que estoy haciendo es capturando los valores por eso uso los (..)
#if matches:
#    last, first = matches.groups()#groups son los ()
#    name = f"{first} {last}"
#print(f"Hello, {name}")

#otra forma para mejorar un poco la lectura del codigo es:
#import re

#name = input("What's your name?").strip()
#matches = re.search(r"^(.+),(.+)$", name)#verificando si el patron ingresado en name es correcto y estan entre (.+),lo que estoy haciendo es capturando los valores por eso uso los (..)
#if matches:
#    last = matches.group(1)# aqui en vez de usar 1 groups son los () , uso 2 individuales que es mejor visualmente, aunque last y first son variables que usaremos una sola vez por lo cual podemos mejorar el codigo aun más
#    first = matches.group(2)
#    name = f"{first} {last}"
#print(f"Hello, {name}")

#nota la convención de group dice que se inicia a contar desde 1 y no desde 0 por eso es que los grupos los nombramos des 1 en adelante
import re

name = input("What's your name?").strip()
matches = re.search(r"^(.+), ?(.+)$", name)#verificando si el patron ingresado en name es correcto y estan entre (.+),lo que estoy haciendo es capturando los valores por eso uso los (..)
if matches:
    name = matches.group(2) + " " + matches.group(1)#aqui estamos concatenando los dos en la variable sangrada name que no la usare
print(f"Hello, {name}")

#puedo usar en matches ? para que ese espacio sea opcional o mejor aún usar * ya  que es un valor o ninguno

# el operador morza o walrus :=, permite asignar un valor y hacer una pregunta boleana

import re

name = input("What's your name?").strip()
if matches := re.search(r"^(.+), ?(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")







