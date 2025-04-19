#re.search(pattern, string , flags = 0),se pueden usar los siguientes patrones
# . any character except a newline ( de la A a la Z , mayúsculas y minúsculas)
# * 0 or more repetition ,dar valor a la izquierda o derecha
# + 1 or more repetition tiene que haber al menos una repeteción
# ? 0 or 1 repetition yo elijo cuantas repeticiones
# {m} m repetitions yo digo cuantas repeticiones
# {m,n} m-n repetitions , mi rango de repeticiones
#S A|B Either A or B  es usar | para decir si es uno el otro
#(...) a group
#(?...) non-capturing version

#re.search(pattern,string, flags = 0)
#las flags ayudan a configurar la función r un poco diferente
#algunas banderas que puedo pasar a la función son:
#re.IGNORECASE , ignorar el caso de la entrada del usuario
#re.MULTILINE , confirgurar los carateres
#re.DOTALL


# A|B tambíen puedo aplicar la mísma para listas de valores
#para que se puedan tolerar subdominios como jromero@madrid.complu.es
#usare ? que significa 0 o 1 repetición , recordar que 0 es infinito 
import re

email = input("What's your email?").strip()
 
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|es|gov|net)$",email, re.IGNORECASE):#(\w+\.)? esto es un sub dominio que en conjunto con ? , dice que se puede o no ejecutar  y podria ingrear direcciones como jromero@gmail.com o direcciones como jromero@madrid.complu.es, (\w+\.)?, todo esto puede o no puede estar allí
    print("Valid")
else:
    print("Invalid")
