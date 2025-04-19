#funcion labda
#names = []

#with open("names.csv") as file:
#    for line in file:
#        nickname , band = line.strip().split(",")
        #como tengo 2 varibles podrdia crear un diccionario creando key and value
#        name = {"nickname":nickname,"band":band}
#        names.append(name)
        
#creo una función que me devuelva el nickname
#def get_name(i):
#    return i["nickname"]  

#python permite usar funciones como argumentos 
#key = get_name , es la foma como ordenara el diccionario
        
#for i in sorted(names, key = get_name):#cmo ya uso la función puedo obtener la llave y ordenarla por sorted
#    print(f"{i['nickname']} like it {i['band']}")


#**********************************************
names = []

with open("names.csv") as file:
    for line in file:
        nickname , band = line.strip().split(",")
        #como tengo 2 varibles podrdia crear un diccionario creando key and value
        name = {"nickname":nickname,"band":band}
        names.append(name)
                    #todo esto es es como la función del código de arrriba solo que no tiene nombre y para 
                    #eso se usa la función lambda ,lambda son funciones anónimas
for i in sorted(names, key= lambda name: name["nickname"] ):
    print(f"{i['nickname']} like it {i['band']}")
    
#lambda, funciones que no necesitan un nombre no tiene el nombre def , pero funcionan igual y permite crearla 
#directamente