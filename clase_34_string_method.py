#__str__ este es un metodo que define dentro de la clase cada vez que queramos ver algo como en cadena 

#class Student:
#    def __init__(self,name,house):#init , función es inicializar un objeto vacío cuando lo llamo 
#        if not name:
#            raise ValueError("Missing name")
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
#        self.name = name #atributos o variables de instancias
#        self.house = house
              

#def main():
#    student = get_student()   
#    print(student)#si trato de imprimit la varable estudent me dara la direccion de la ubicación temporal donde se creo la instancia que <__main__.Student object at 0x00000298B6180350>, para ver que realmente se cree se usa la el constructos __str__
      
    
#def get_student():
#    name = input("Name: ").strip().title()#atributos
#    house = input("House: ").strip().title()#atributos
#    return Student(name,house)
    
       
#if __name__ == "__main__":
#    main()
    
#para solucionar eso se creara una función que nos ayude a la creación de string
#class Student:
#    def __init__(self,name,house):#init , función es inicializar un objeto vacío cuando lo llamo 
#        if not name:
#            raise ValueError("Missing name")
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
#        self.name = name #atributos o variables de instancias
#        self.house = house
              
#    def __str__(self):
#        return f"{self.name} from {self.house}"

#def main():
#    student = get_student()   
#    print(student)#si trato de imprimit la varable estudent me dara la direccion de la ubicación temporal donde se creo la instancia que <__main__.Student object at 0x00000298B6180350>, para ver que realmente se cree se usa la el constructos __str__, cuando imprimo esto me llamara al constuctor de la clase
      
    
#def get_student():
#    name = input("Name: ").strip().title()#atributos
#    house = input("House: ").strip().title()#atributos
#    return Student(name,house)
    
       
#if __name__ == "__main__":
#    main()
    
#ahora avanzando un poco más con el código , le ingresare el Patronus 

class Student:
    def __init__(self,name,house,patronus):#init , función es inicializar un objeto vacío cuando lo llamo 
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name #atributos o variables de instancias
        self.house = house
        self.patronus = patronus
              
    def __str__(self):
        return f"{self.name} from {self.house}  patronus  {self.patronus}"

def main():
    student = get_student()   
    print(student)      
    
def get_student():
    name = input("Name: ").strip().title()#atributos
    house = input("House: ").strip().title()#atributos
    patronus = input("Patronus: ").strip().title()#atributos
    return Student(name,house,patronus)
    
       
if __name__ == "__main__":
    main()
    
