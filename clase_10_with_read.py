#con esto escribo
#name = input("What's your name? ")

#with open("names.txt","a") as file:
#    file.write(f"{name} \n ")

#ahora leere el archivo con with
#with open("names.txt","r") as file:#usamos r para lectura Read  
#    lines = file.readlines()#creo la variable lines y uso la funcion readlines
    
#ahora como ya tengo las los files en la variable lines voy a iterar para imprimirlos
#for line in lines:
#    print("Hello, " , line)#salen espacios entre lineas ya que el simbolo de impresión añade una linea
    #adicional , para solucionarlo podria hacer esto
    #print("Hello,", line, end= "")# o mucho mejor es usar strip
#    print("Hello,", line.rstrip())
    
#mejorando el código, pero solo para imprimir
#with open("names.txt","r") as file:
#    for line in file:
#        print("Hello,",line.rstrip())

#creando el código pero que en este caso me permita ordenarlo primero
#names = [] #creo una lista para especificar el orden que quiero

#with open("names.txt")as file:# como no use "r" ,solo lo estoy abriendo y no lo edito
#    for line in file:
#        names.append(line.rstrip().title().strip())#agrego lo que ya tengo en 
# names txt y lo limpio

#for name in sorted(names):
#    print(f"Hello, {name}")

    
#ahora si solo lo quiero ordenado podria mejorar el código asi y ordenarlo directamente del mismo archivo
#with open("names.txt")as file:# como no use "r" ,solo lo estoy abriendo y no lo edito
#    for line in file:
#        print("Hello,",line.strip().title().strip())
        
#usando la función reverse para que para que se ordene de z ha a
#reverse = False , por naturaleza para que funcione debe hacerse True
names = [] #creo una lista para especificar el orden que quiero

with open("names.txt")as file:# como no use "r" ,solo lo estoy abriendo y no lo edito
    for line in file:
        names.append(line.rstrip().title().strip())#agrego lo que ya tengo en names txt y lo limpio

for name in sorted(names, reverse= True):#usando reverse para que funciones
    print(f"Hello, {name}")

