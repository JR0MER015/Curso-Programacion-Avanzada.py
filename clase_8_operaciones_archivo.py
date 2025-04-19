#file I/O , achivos de entra o salida
#guardar archivos de los progrmas que cófifico
#usando listas para archivar varios valores 

names =  []

for _ in range(3):#pueso usar i como variable para iterar pero como es una varible que no voy a usar uso _
    #name = input("What's your name? ")
    #names.append(name)
    #modificando los dos líneas en una sola
    names.append(input("What's your name? "))
    
#ordenar la lista para impreción
for name in sorted(names):
    print(f"Hello,{name}")

#función open que sirve para guardar o abrir archivos que hemos usado

name = input("What's your name? ")#ingreso 
file = open(name("names.txt","w"))
