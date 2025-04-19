#generators, crear valores con funciones ,para no quedarme sin memoria

#n = int(input("What's n?"))

#for i in range(n):
#    print("oveja mememe\n" * i , end= "")
    
    
#ahora quiero hacer este código una función
#def main():
#    n = int(input("What's n?"))

#    for i in range(n):
#        print("oveja mememe\n" * i , end= "")
        
#if __name__ == "__main__":
#    main()
    
#ahora puedo hace que la función principal tenga una funcion adicional como una prueba de valor
#def main():
#    n = int(input("What's n?"))

#    for i in range(n):
#        print(sheep(i) , end= "")
        
#def sheep(n):
#    return "oveja mememe\n"
        
#if __name__ == "__main__":
#    main()
    
#como no se cuantas ovejas se necesitan vamos a crear un rebaño de ovejas
#def main():
#    n = int(input("What's n?"))

#    for s in sheep(n):
#        print(s, end= "")
        
#def sheep(n):
#    flock =[]
#    for i in range(n):
#        flock.append("oveja mememe\n")
#    return flock
    
        
#if __name__ == "__main__":
#    main()
    
#ahora el problema es que si imprimo muchos valores me quedare sin memoria ,para eso usamos generators
#yield es la función que vamos a usar

def main():
    n = int(input("What's n?"))

    for s in sheep(n):
        print(s, end= "")
        
def sheep(n):
    for i in range(n):
        yield "oveja mememe\n" #devolver un valor a la vez asi que esto optimiza el ptoceso
    
    
       
if __name__ == "__main__":
    main()

#esta función devuelve lo que llamaremos un iterators que tu código genere un valor a la vez, devolviendolo inmediatament.en el caso anterior primero lo crea y despues lo crea.
#en cada valor devuelve el valor para que la memoria no se trave
#en cualquier caso para cancelar el proceso uso control c










