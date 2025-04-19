# se crea un archivo csv, que es un archivo separados por comas
#cree un archivo csv que muestre el nombre y mas datos pero las listas de comas estan diferentes añadidas , nuestran que hay diferencias entre los valores y llaves que quiero

#name = input("What's your name and address  ")#ingreso de información

#file = open("names1.csv","a")#a, es append que hace que se añada cada vez que se usa 
#file.write(f"{name} \n ") #con eso soluciono el problema de la linea 9 ya que añadi espacios
#file.close()#cierro el archivo

#students = []

#with open("names1.csv") as file:
#    for line in file:
#        name , home = line.strip().split(",")
        #como tengo 2 varibles podrdia crear un diccionario creando key and value
#        student = {"name": name,"Home":home}
#        students.append(student)
                    #todo esto es es como la función del código de arrriba solo que no tiene nombre y para 
                    #eso se usa la función lambda ,lambda son funciones anónimas
#for i in sorted(students, key= lambda student: student["name"] ):
#    print(f"{i['name']} like it {i['home']}")
    
#esto da un error de valor ValueError,dado por la linea 14 ya que me devuelve mas valores de los que estoy pidieno
#si tengo un problema es probable que alquien más lo haya tenido por lo que existen librerias para documentos csv que me haran la vida mas facil, cambiaremos el código un poco para hacerlo funcionar con la libreria csv

import csv

students = []

with open("names1.csv") as file:
    reader = csv.reader(file)#función reader de la libreia csv , que lee el achivo y sabe donde estan las comas y te permite iterar no en la función si no directamente en el archivo csv
    #for row in reader:
    #    students.append({"name":row[0], "home": row[1]})
    #también podemos usar directamente el código asi
    #name , home = line.strip().split(",")
        #como tengo 2 varibles podrdia crear un diccionario creando key and value
    #    student = {"name": name,"Home":home}
    #    students.append(student)
    #esta ultima función no me dio por lo cual la estoy iterando con el if mas abajo
    
    for row in reader:
        if len(row) >= 2:
            students.append({"name": row[0], "home": row[1]})
        #else:
        #    print(row.splic())
    
    
for i in sorted(students, key= lambda student: student["name"] ):
    print(f"{i['name']} is from {i['home']}")






