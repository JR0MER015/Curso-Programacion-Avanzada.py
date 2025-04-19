#función open que sirve para guardar o abrir archivos que hemos usado

name = input("What's your name? ")#ingreso de información

#estas 3 lineas es commo dar click y crear un archivo y editarlo y cerrarlo
#file = open("names.txt","w")#aqui creo el archivo , la W significa que voy a escribir Write
#con "w" hay un problema que es que solo escribe actualiza, para eviat esto uso mejot "a" append
#file = open("names.txt","a")#a, es append que hace que se añada cada vez que se usa 
#problema es que salen pegados 
#file.write(name)#escribo en el archivo
#file.write(f"{name} \n ") #con eso soluciono el problema de la linea 9 ya que añadi espacios
#file.close()#cierro el archivo

#en caso que se me olvide usar el file.close() puedo usar with

with open("names.txt","a") as file:
    file.write(f"{name} \n")
