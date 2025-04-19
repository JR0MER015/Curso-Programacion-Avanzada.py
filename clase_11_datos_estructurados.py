# se crea un archivo csv, que es un archivo separados por comas
#cree un archivo csv que muestre el nombre y la banda 

#name = input("What's your name? ")#ingreso de información

#file = open("names.csv","a")#a, es append que hace que se añada cada vez que se usa 
#file.write(f"{name} \n ") #con eso soluciono el problema de la linea 9 ya que añadi espacios
#file.close()#cierro el archivo

#como ya cree el archivo ahora puedo usar with open e iterar las listas
#names = [] #creo una lista para especificar el orden que quiero

#with open("names.csv")as file:# uso el archivo csv que ya he creado con with open
#    for line in file:
#        #row = line.rstrip().title().strip().split(",")#agrego lo que ya tengo en names txt y lo limpio
#        name, band = line.rstrip().split(",")# ya que estoy usando split puedo cambiar la variable
#        #y con eso tener dos variables mas y mas facil de imprimir
#        print(f"{name} like it {band}")#me da un error de ValueError asi que usare una validación
#ValueError es un error de dato que algo esta mal ingresado
        

#with open("names.csv")as file:# uso el archivo csv que ya he creado con with open
#    for line in file:
#        #row = line.rstrip().title().strip().split(",")#agrego lo que ya tengo en names txt y lo limpio
#        parts = line.rstrip().split(",")# ya que estoy usando split puedo cambiar la variable
#        #y con eso tener dos variables mas y mas facil de imprimir
#        if len(parts) == 2:
#            name, band = parts
#            print(f"{name} like it {band}")
#        else:
#            print(f"Linea invalidada: {line}")

#ahora creare una lista que me de la información del archivo csv en orden

#names = []

#with open("names.csv") as file:
#    for line in file:
#        non , band = line.strip().split(",")
#        names.append(f"{non} like it {band}")

#ahora iterare la lista 
#for i in sorted(names):
#    print(i)
    
#mejorando el código para que no ordene por la oración si  línea 40 , si no por el nombre
#names = []

#with open("names.csv") as file:
#    for line in file:
#        nickname , band = line.strip().split(",")
        #como tengo 2 varibles podrdia crear un diccionario creando key and value
#        name = {} # creo un diccionario vacio
#        name["nickname"] = nickname
#        name["band"] = band
#        names.append(name)
        
#for i in names:
#    print(f"{i['nickname']} like it {i['band']}") # uso comillas simples para que python diferencie el uso,
    #recordando que los diccionarios se llaman por strings

#pero aun no estan ordenadas
#mejorando el codigo
#names = []

#with open("names.csv") as file:
#    for line in file:
#        nickname , band = line.strip().split(",")
        #como tengo 2 varibles podrdia crear un diccionario creando key and value
#        name = {"nickname":nickname,"band":band}
#        names.append(name)
        
#for i in names:
#    print(f"{i['nickname']} like it {i['band']}")
    
#los diccionarios no los podemos ordenar por sorted(names)
#lo que usares es una clasificación de llave
names = []

with open("names.csv") as file:
    for line in file:
        nickname , band = line.strip().split(",")
        #como tengo 2 varibles podrdia crear un diccionario creando key and value
        name = {"nickname":nickname,"band":band}
        names.append(name)
        
#creo una función que me devuelva el nickname
def get_name(i):
    return i["nickname"]  #puedo usar cualquier nombre o usar el nombre del diccionario en este caso podria ser name

#python permite usar funciones como argumentos 
#key = get_name , es la foma como ordenara el diccionario
#for i parece igual al i de la función pero son diferentes por eso pueso usar otro nombre en for en vez e i ejemplo elemento["nickname
# "]
        
for i in sorted(names, key = get_name):#cmo ya uso la función puedo obtener la llave y ordenarla por sorted
    print(f"{i['nickname']} like it {i['band']}")

        
