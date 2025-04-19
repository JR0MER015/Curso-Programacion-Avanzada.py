#constantes, variables que se les asigna el valor no lo puedes cambiar 
#pero esto es por sistema de Honor
#cuando tengo una constante debo hacerlo que me muestre mas 
#for i in range(3):
#    print("meow")

#si sigo programdo y uso otro 3 y tengo un error es posible que no sepa donde esta el 3 que busco , por lo cual podria hacer esto

#MEOWS = 3

#for _ in range(MEOWS):
#    print("meows")
    
#poner en mayúsculas las varibles que son constantes en PYTHON
#o usar poo

class Cat:
    MEOW = 3
    
    def meow(self):
        for _ in range(Cat.MEOW):
            print("meow")
            
cat = Cat()
cat.meow()