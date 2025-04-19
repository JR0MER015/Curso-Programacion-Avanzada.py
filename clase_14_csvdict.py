#lecturas de archivos csv , para que actualilcen en la misma lista de datos


#cree un archivo csv que muestre el nombre y mas datos pero las listas de comas estan diferentes añadidas , nuestran que hay diferencias entre los valores y llaves que quiero

#name = input("What's your name and address  ")#ingreso de información

#file = open("names2.csv","a")#a, es append que hace que se añada cada vez que se usa 
#file.write(f"{name} \n ") #con eso soluciono el problema de la linea 9 ya que añadi espacios
#file.close()#cierro el archivoM

#he creado un archivo #2 con nombres y direccines
#ahora puedo modificar el archivo csv directamente y ponerle los encabezados que quiero en este caso seria nombre y  dirección 


import csv

students = []

with open ("names2.csv") as file:
    reader = csv.DictReader(file)#es un lecctor de diccionario que me permite iterarlo si escribo las claves en las lineas 1 del archivo csv 
    for row in reader:
        students.append({"name":row["name"], "home": row["home"]})#estoy llamando valores desde un diccionario
        
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
    
#nota cuidado al ingresar los valores debes tener cuidado con los espacios en blaco y las cadenas si no no funciona

#hora si el usuario cambia los valores cambia el archivo csv el archivo seguira funcionando 
#los códigos de diccionaros son mas dificiles de romper si el key es siempre el mismo

#ota foma de hacerlo es asi 
"""
import csv

students = []

with open ("names2.csv") as file:
    reader = csv.DictReader(file)#es un lecctor de diccionario que me permite iterarlo si escribo las claves en las lineas 1 del archivo csv 
    for row in reader:
        students.append(row)#estoy llamando valores desde un diccionario
        
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

"""



