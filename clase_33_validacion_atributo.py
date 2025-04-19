#si quiero validar atributos en clases 
#puedo crear tantas instancias de clases como quiero y validarlas tambien podria usar house= None para el caso en que no se necesite se muestre None

class Student:
    def __init__(self,name,house):#init , función es inicializar un objeto vacío cuando lo llamo 
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name #atributos o variables de instancias
        self.house = house
              

def main():
    student = get_student()   
    print(f"{student.name} is from {student.house}")#uso de comillas simples y dobles
      
    
def get_student():
    name = input("Name: ").strip().title()#atributos
    house = input("House: ").strip().title()#atributos
    return Student(name,house)
    
       
if __name__ == "__main__":
    main()