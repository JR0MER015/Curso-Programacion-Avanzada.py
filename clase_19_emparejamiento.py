#en expresiones R podemos decidir como comienza y termina un valor 
# ^ matches the start of the string
# $ matches the end of the string on  just before the newline at the end of the string

#import re

#email = input("What's your email?").strip()

#if re.search(r"^.+@.+\.edu$",email):#le estoy diciendo la exprecion regular que inicie con ^ y termine con $, ahora si ingreso cosas en la terminal como : my name is jromero@madrid.edu , sera invalido 
#    print("Valid")
#else:
#    print("Invalid")

#el problema es que "." permite culaquier cosa y debo ser  mas restrigtivo para que el usuario ingrese solo lo que se necesita
#Juego de caracteres, las expresiones regulares tambien soportan estos caracteres
# [] set of characters, incluir uno o mas caracteres que quiero
# [^] complementing the set ,es decir no puede iniciar por eso

#import re

#email = input("What's your email?").strip()

#if re.search(r"^[^@,^.,^¡]+@[^@]+\.edu$",email):#corchetes caracteres validos , [^] valores invalidos
#    print("Valid")
#else:
#    print("Invalid")
    
#mejorando el código para decir que puedo tolerar
#import re

#email = input("What's your email?").strip()

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):#lo que quiero que se ingrese pero sin comas o separadores,todos los carácteres que puedo recibir 
#    print("Valid")
#else:
#    print("Invalid")
    
#esta es la mejor espresión para expresiones regulares, sin embargo se puede hacer mediante atajos que ya estan determinados en expresiones regulares para que el código se vea aun mejor:
#\d decimal digit
#\D not a decimal 
#\s whitespace characters
#\S not a whitespace characters
#\w word characters as well as numbers and teh underscore(guión bajo)
#\W not a word characters
#S A|B Either A or B  es usar | para decir si es uno el otro
#(...) a group
#(?...) non-capturing version

#con esto vamos a mejorar el codigo de arriba
import re

email = input("What's your email?").strip()

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):#lo que quiero que se ingrese pero sin comas o separadores,todos los carácteres que puedo recibir 
if re.search(r"^\w+@\w+\.(edu|com|es|gov|net)$",email):#es exactamente lo mismo que arriba pero con los atacos de convención, tambien puedo usar una grupo de valores en los cuales puede terminar listados por un match
    print("Valid")
else:
    print("Invalid")
    
#usando banderas para para mejoarar la codificación.
#re.search(pattern,string, flags = 0)
#las flags ayudan a configurar la función r un poco diferente
#algunas banderas que puedo pasar a la función son:
#re.IGNORECASE
#re.MULTILINE
#re.DOTALL

    

