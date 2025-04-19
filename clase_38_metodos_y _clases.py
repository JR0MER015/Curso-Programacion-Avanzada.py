#class methods, funcionalidad diferente independientemente de los valores de la clase
#@classmethod :metodo no tiene acceso a si mismo ,pero si sabe dentro de que clase esta 
#haremos un programa de un sombrero seleccionador 

#class Hat:
#    def sort(self,name):
#        print(name, "is in", "some house")
    

#hat = Hat()# instanciar una clase
#hat.sort("Harry")

#ahora creo el constructor para que clasifique las casas 
#class Hat:
#    def __init__(self):
#        self.houses = ["Gryffinfor","Hufflepuff","Ravenclaw","Slytherin"]
        
#    def sort(self,name):
        #house = random.choice(self.houses)
#        print(name, "is in", random.choice(self.houses))#no me funciona random.choice ya que no importe la biblioteca
    

#hat = Hat()# instanciar una clase
#hat.sort("Harry")

#ahora realizo la importación de la biblíoteca para quitar el error 
#import random

#class Hat:
#    def __init__(self):
#        self.houses = ["Gryffinfor","Hufflepuff","Ravenclaw","Slytherin"]
        
#    def sort(self,name):
        #house = random.choice(self.houses)
#        print(name, "is in", random.choice(self.houses))#no me funciona random.choice ya que no importe la biblioteca
    

#hat = Hat()# instanciar una clase
#hat.sort("Harry")

#se debe usar una clase cuando se quiere representar algo en el mundo real o imaginario
#ahora recordemos que solo hay un sombrero en la pelicula, pero se podria ampliar, lo que vamos hacer es mejorar el metodo para que unícamente sea uno solo y sin necesidad de instanciarlo,para eso usamos @classmethod, que es otro decorados 

#import random

#class Hat:
    #def __init__(self):ya no lo ocupo ya que init es para inicializar las clases 
#    houses = ["Gryffinfor","Hufflepuff","Ravenclaw","Slytherin"] #ahora lo creo como una variable de clases
     
#    @classmethod #definiendo que solo hay un objeto   
#    def sort(cls,name):#ya no ocupas el self , asi que usamos cls que es para el decorador unico        
#        print(name, "is in", random.choice(cls.houses))
    

#hat = Hat()# instanciar una clase ya no es necesaria ya que estoy usando el decorador classmethod
#Hat.sort("Harry")#ahora ingreso al metodo de clases, usando el nombre de la clase

#las clases ayuddan a que el código se mantenga mas organizado y a medida esto se va ampliando este se mantenga más ordenado

#ahora vamos a mejorar el código del estudiante


class Student:
    def __init__(self,name,house):
        self.name = name #atributos o variables de instancias
        self.house = house
                  
    def __str__(self):
        return f"{self.name} from {self.house} "
    
    @classmethod #puedo llamar este metodo sin instanciarlo 
    def get(cls):#referencia a la propia clase
        name = input("Name: ").strip().title()
        house = input("House: ").strip().title()
        return cls(name,house)
        
    

def main():
    student = Student.get() #he movido el código dentro de la clase ya que es ordenado al crear el objeto
    print(student)      
    
       
if __name__ == "__main__":
    main()