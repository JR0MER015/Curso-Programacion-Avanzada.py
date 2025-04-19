#ordenando funciones principales para tener un codigo mas limpio

#def main():#funcion principal
#    name = str(input("What is your name?: ")).strip().title()
#    hello(name)
    
#def hello(to = "world"):#to puede ser name tambien
#    print("Hello,", to)
    
#main()

#scope(ambito), una funcion solo existe si se ha definido 

#definiendo una función cuadrado
def main():
    x = int(input("What is X ?: "))
    print("X cuadrado is", cuadrado(x))
  
#Un cuadrado es un numero multiplicado por si mismo  
def cuadrado(n): #N es una varible de cualquier numero
    #return pow (n,2)#formula para elevación
    return n * n # si quiero elevar a la potencia seria **
print("se esta ejecutando el modulo")

if __name__ == "__main__":#añadido para en la calse 7 de unit test por buena constumbre al llamar 
    #funciones
    main()    
#main()