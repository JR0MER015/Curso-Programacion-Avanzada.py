#regular expression o regexes, es común para tener patrones y identificarlos para saber que patrones y datos estamos recibiendo por las personas

#email = input("What's your email?").strip()

#if "@" in email:
#    print("Valid")
#else:
#    print("Invalid")
    
#el probelma es que si solo escribo @ ya funciona debo darle una validación mas

#email = input("What's your email?").strip()

#if "@" in email and "." in email:
#    print("Valid")
#else:
#    print("Invalid")

#aqui todavia sigo con el problema ya que solo puedo poner @. o inverso y fucniona
#utilizare una nueva lógica  usando

#email = input("What's your email?").strip()

#username, domain = email.split("@")#con el split divido las dos en dos variables 

#if (username) and ("." in domain):#esto lo que hace es validar que username sea algo y no ninguno tiene que ser algo , aqui se comparan dos Boleanos(TRUE o FALSE)
#    print("Valid")
#else:#si no tiene caracteres sera falso
#    print("Invalid")
    
#pero lo podemos hacer mas precisos 

email = input("What's your email?").strip()

username, domain = email.split("@")#con el split divido las dos en dos variables 

if username and domain.endswith(".edu"):#revisa las dos variables y los valores Boleanos , asi mismo la función endswith() revisa que el valor termina con la tabla
    print("Valid")
else:#si no tiene caracteres sera falso
    print("Invalid")
    
#igual con problema ya que puedo poner jromero@.edu
#para mejorar esto hay una biblioteca que ayuda a validar y revisar valores repetitivos
#Libreria RE 
