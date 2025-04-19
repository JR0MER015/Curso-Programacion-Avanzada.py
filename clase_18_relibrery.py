#usando la libreía RE, en especifico la funcion de busqueda 
#re.search(pattern, string , flags = 0),esta es la estructura de la función 

#import re

#email = input("What's your email?").strip()

#if re.search("@",email):#usando la funcion re.search de busqueda
#    print("Valid")
#else:
#    print("Invalid")
    
#esta es la primera validación para comprobar que el código funciona , pero podemos usar mas vocabulario
#re.search(pattern, string , flags = 0),se pueden usar los siguientes patrones
# . any character except a newline ( de la A a la Z , mayúsculas y minúsculas)
# * 0 or more repetition ,dar valor a la izquierda o derecha
# + 1 or more repetition tiene que haber al menos una repeteción
# ? 0 or 1 repetition yo elijo cuantas repeticiones
# {m} m repetitions yo digo cuantas repeticiones
# {m,n} m-n repetitions , mi rango de repeticiones

#import re

#email = input("What's your email?").strip()

  #if re.search(".*@.*",email):#usando la funcion re.search de busqueda @ , "." me dara valores de A-Z , *buscara los valores a mi izquierda o derecha pero * busca 0 o 1 repetición y eso dejara pasar cosas
#    print("Valid")
#else:
#    print("Invalid")

#ya que uso * me deja pasar cosas como jromero@ ya que * es 0 o 1 repetición por lo cual debo usar +,aunque se puede usar también asi if re.search("..*@..*",email) ya que el "." me validara dos veces lo que tenga 

#import re

#email = input("What's your email?").strip()

#if re.search(".+@.+",email):#usando la funcion re.search de busqueda @ , "." me dara valores de A-Z , +buscara los valores a mi izquierda o derecha cuya repetición inicie por 1 , es decir debe encontrar un valor , es lo mismo que usar if re.search("..*@..*",email)
#    print("Valid")
#else:
#    print("Invalid")

#modificando el código para que valide la terminación en ".edu",pero recordando que "." signigica cualquier cosa 

import re

email = input("What's your email?").strip()

if re.search(r".+@.+\.edu",email):#usando la funcion re.search de busqueda @ , "." me dara valores de A-Z , +buscara los valores a mi izquierda o derecha cuya repetición inicie por 1 , es decir debe encontrar un valor , es lo mismo que usar if re.search("..*@..*",email), si uso (".+@.+.edu",email)me dejara entrar cualquier cosa ya que el ". " esta interpretando como cualquir cosa antes de edu por lo cual dejaría pasar cosas como jromero@gmail?.edu,para solucionar esto puedo usar la barra nueva linea \ para que me lo tome una nueva linea de de validación al finalizar los valores en .edu. R significa un regla para que python interprete esto como una cadena independiente  y no interprete \ como una nueva línea mas , si no como una nueva validación ,seria fimilar a una cadema "f" nada mas que esta es una cadena "r" cadenas sin fomatos son usadas para validación de expreciones 
    print("Valid")
else:
    print("Invalid")


