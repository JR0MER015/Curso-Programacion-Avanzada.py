#class Student:
#    def __init__(self,name,house):#init , función es inicializar un objeto vacío cuando lo llamo 
#        if not name:
#            raise ValueError("Missing name")
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
#        self.name = name #atributos o variables de instancias
#        self.house = house
        
              
#    def __str__(self):
#        return f"{self.name} from {self.house} "

#def main():
#    student = get_student()   
#    print(student)      
    
#def get_student():
#    name = input("Name: ").strip().title()#atributos
#    house = input("House: ").strip().title()#atributos
#    return Student(name,house)
    
       
#if __name__ == "__main__":
#    main()
    
#una properties , son mecanismos de defensa para que no se puedan ingresar cosas cosas,usando @propertie tambien estan los decorators de funciones , son funciones que modifican el comportamiento de otras funciones
#class Student:
#    def __init__(self,name,house):#init , función es inicializar un objeto vacío cuando lo llamo 
#        if not name:
#            raise ValueError("Missing name")
#        self.name = name #atributos o variables de instancias
#        self.house = house
        
              
#    def __str__(self):
#        return f"{self.name} from {self.house} "
    
    #Getter
    #definienfo un método que me regrese el nombre de la casa
    #getter, es una función de una clase que obtiene atributos
    
    #los getter y setter son instrucciones para que el programador no ingrese código que no corresponda con los atributos definidos y ayuda a validar ingreso de información ,tener control de lo que se ingresa, ayuda a detectar valores 
    #con getter es un argumento y con setter son 2 argumentos,getter se usa @property y con el seter es argumento.setter
    
#    @property
#    def house(self):#siempre debe haber un argumento self
        #return self.house # se usa self._house para que no choque con el mismo nombre del atributo ya que no puedo tener fuciones y variables con el mismo nombre
#        return self._house
    
    #Setter
    #setter,es una funcion en una clase que obtener un valor
#    @house.setter
#    def house(self,house):
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid House")
        #self.house = house
#        self._house = house
        
    

#def main():
#    student = get_student() 
    #student.house = "Number Four,Privet Drive"#el setter simpre sera llamado aunque yo intenta cmabiar el atgumento , por lo cual levantara el error ValueError Invalid House
#    print(student)      
    
#def get_student():
#    name = input("Name: ").strip().title()#atributos
#    house = input("House: ").strip().title()#atributos
#    return Student(name,house)
    
       
#if __name__ == "__main__":
#    main()
    
#creando un nuevo setter y getter 

class Student:
    def __init__(self,name,house):#init , función es inicializar un objeto vacío cuando lo llamo 
        #if not name:
        #    raise ValueError("Missing name")# esta validación ya no es necesaria ya que creo el setter y su getter para los atributos
        self.name = name #atributos o variables de instancias
        self.house = house
        
              
    def __str__(self):
        return f"{self.name} from {self.house} "
    
    #estableciendo un setter para name
    @property
    def name(self):
        return self._name
    
    #ahora creo el setter
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name#variable de instancias 
                
    @property
    def house(self):#siempre debe haber un argumento self
        #return self.house # se usa self._house para que no choque con el mismo nombre del atributo ya que no puedo tener fuciones y variables con el mismo nombre
        return self._house
    
    #Setter
    #setter,es una funcion en una clase que obtener un valor
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        #self.house = house
        self._house = house
        
    

def main():
    student = get_student() 
    #student.house = "Number Four,Privet Drive"#el setter simpre sera llamado aunque yo intenta cmabiar el atgumento , por lo cual levantara el error ValueError Invalid House
    #student._house = "Number Four,Privet Drive", aqui si pofria entrear ya que estaria ingresando a la variable de isntancia , lo que se hace es el código de honor en el cual se establece que ._ es algo que no puedes acceder y debes tener cuidado.
    print(student)      
    
def get_student():
    name = input("Name: ").strip().title()#atributos
    house = input("House: ").strip().title()#atributos
    return Student(name,house)
    
       
if __name__ == "__main__":
    main()