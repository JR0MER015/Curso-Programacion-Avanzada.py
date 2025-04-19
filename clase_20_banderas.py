#import re

#email = input("What's your email?").strip()

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):#lo que quiero que se ingrese pero sin comas o separadores,todos los carácteres que puedo recibir 
#if re.search(r"^\w+@\w+\.(edu|com|es|gov|net)$",email):#es exactamente lo mismo que arriba pero con los atacos de convención, tambien puedo usar una grupo de valores en los cuales puede terminar listados por un match
#    print("Valid")
#else:
#    print("Invalid")
    
#usando banderas para para mejoarar la codificación.
#re.search(pattern,string, flags = 0)
#las flags ayudan a configurar la función r un poco diferente
#algunas banderas que puedo pasar a la función son:
#re.IGNORECASE , ignorar el caso de la entrada del usuario
#re.MULTILINE , confirgurar los carateres
#re.DOTALL

import re

email = input("What's your email?").strip()

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):#lo que quiero que se ingrese pero sin comas o separadores,todos los carácteres que puedo recibir 
if re.search(r"^\w+@\w+\.(edu|com|es|gov|net)$",email, re.IGNORECASE):#es exactamente lo mismo que arriba pero con los atajos de convención, tambien puedo usar una grupo de valores en los cuales puede terminar listados por un match, la validación con re.IGNORECASE, lo que hace es dejar pasar al usuario si escribe por ejemplo al el domin o la dirección al final en mayúscula.
    print("Valid")
else:
    print("Invalid")