
#importare la libreria RE ya trabajar con regular string
#en especifico una que se llama re.sub(pattern, repl, string, count=0 flags = 0)
#pattern = patron , es la string que debo buscar
#repl = es el valor con el que voy a remplazar
#string= argumentos con los que voy a sustituir 
#count = cuantas veces se debe cambiar en la bussqueda


#import re

#url = input("URL:").strip()

#username = re.sub(r"https://twitter.com//", "",url)

#print(f"Username: {username}")

#ya funciona pero hay un problema con los protocolos y con la entrada de subcaracteres
#resolviendo algunos de esos problemas 
#recordar que cada vez que algo incluya "." o caracteres especiales hay que referenciarlos con \ caso contrario sera tomado como un caracter que tome todo lo que se ingrese
#re.sub es para limpiesa de datos 

import re

url = input("URL:").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com//", "",url)#?puede o no estar ()? valido el conjunto y puede o no puede estar

print(f"Username: {username}")

