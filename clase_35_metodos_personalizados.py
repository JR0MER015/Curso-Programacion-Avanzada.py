#métodos personalizados, puedentener variables o valiables de estancias , metodos y funciones, los metodos son funciones dentro de las clases


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
    
    #creo mi propio metodo , que se en realidad es un función dentro de la clase
    def charm(self):#aqui ya esta creado mi propio método o función uso ... para establecer que posteriormente sera definido.
        ...

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
    


#aqui ya esta el código con el método creado y con match que crea verifica concordancias
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
    
    #creo mi propio metodo , que se en realidad es un función dentro de la clase
    def charm(self):#aqui ya esta creado mi propio método o función uso ... para establecer que posteriormente sera definido.
        match self.patronus:
            case "Stag":
                return "Ciervo"
            case "Otter":
                return "Nutria"
            case "Jack Russel Terrier":
                return "Perro"
            case _:#casae _ significa para todo lo demas que no este contemplado
                return "Nada por ahora"

def main():
    student = get_student()   
    print("Expecto Patronum")
    print(student.charm()) #llamo al método fuera de la función     
    
def get_student():
    name = input("Name: ").strip().title()#atributos
    house = input("House: ").strip().title()#atributos
    patronus = input("Patronus: ").strip().title()#atributos
    return Student(name,house,patronus)
    
       
if __name__ == "__main__":
    main()