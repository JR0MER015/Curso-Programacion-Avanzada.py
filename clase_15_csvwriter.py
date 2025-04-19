#escritor de archivos csv , para que actualilcen en la misma lista de datos


#cree un archivo csv que muestre el nombre y mas datos pero las listas de comas estan diferentes añadidas , nuestran que hay diferencias entre los valores y llaves que quiero

#name = input("What's your name and address?").strip()#ingreso de información

#file = open("names3.csv","a")#a, es append que hace que se añada cada vez que se usa 
#file.write(f"{name} \n ") #con eso soluciono el problema de la linea 9 ya que añadi espacios
#file.close()#cierro el archivo

#he creado un archivo #3 con nombres y direccines
#ahora puedo modificar el archivo csv directamente y ponerle los encabezados que quiero en este caso seria nombre y  dirección 


#import csv

#name = input("What is yor name?").strip()
#home = input("Where is your home?").strip()

#with open ("names3.csv",'a') as file:#uso "a"= append ya que quiero que se añadan al archivo csv
#    writer = csv.writer(file)#es un lecctor de diccionario que me permite iterarlo si escribo las claves en las lineas 1 del archivo csv 
#    writer.writerow([name, home])
    
#nota cuidado con la actualización de los archivos ya que no se me mostraba nada 

#usano el dict reader
import csv

name = input("What is yor name?").strip()
home = input("Where is your home?").strip()

with open ("names3.csv",'a') as file:
    
    
    writer = csv.DictWriter(file, fieldnames=["name","home"])  #asi mismo hay que darle el orden de los campos
    writer.writerow({"name":name, "home":home,}) #el excel o csv debe tener los mismos encabezados para que sea un diccionario 






























