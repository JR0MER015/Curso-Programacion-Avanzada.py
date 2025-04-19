#__init__ es un metodo de instancia diseñado por Python , __init__ tambien ayuda a guardar temporalmente los objetos que hemos creado para que sean llamados 
#diferencia entre init y el contructos Student(name,house) de la función get_student , se da ya que init inicializa el contenido y el constructor lo crea

#class Student:
#    def __init__(self,name,house):#init , función es inicializar un objeto vacío cuando lo llamo 
#        self.name = name #atributos o variables de instancias
#        self.house = house
              

#def main():
#    student = get_student()   
#    print(f"{student.name} is from {student.house}")#uso de comillas simples y dobles
      
    
#def get_student():
#    name = input("Name: ").strip().title()#atributos
#    house = input("House: ").strip().title()#atributos
#    return Student(name,house) #función que llama al constructor init
    #asiendo el código más eficiente validando los el ingreso de datos.
    
#if __name__ == "__main__":
#    main()
    
#en python hay una función que permite realizar excepciones de errores u omisiones que pueden pasar en este caso una de ellas es RAISE. ayuda a alertar al programador que algo a susedido 
#en este caso usare RAISE, para un caso en que se olvida el nombre

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
    
    #tambien puedo crear estas validaciones 
    #try:
    #    return Student(name,house) #función que llama al constructor init,si se ingresan los valores pasaran caso contrario van al except
    #asiendo el código más eficiente validando los el ingreso de datos.
    #except:
    #    ...
    
if __name__ == "__main__":
    main()