#hay otroa decoradores que son estaticos como @staticmethod , pero la mejor caracteristica de poo es inheritance , tomar metodos y variables de un padre.

#class Student:
#    def __init__(self,name,house):
#        self.name = name
#        self.house = house
    
#    ...
    
#class Professor:
#    def __init__(self,name,subject):
#        self.name = name
#        self.subject = subject
        
#problema hasta aqui es que tengo variables similares y estoy usando el constructor __init__ varias veces , para eso vamos heredar y mejorar el código
#tanto el estudiante como el profesor son magos asi que se crea una clase padre llamado mago

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        
    def __str__(self):
        return f"Wizard: {self.name}"


class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house
        
    def __str__(self):
        return f"Student: {self.name}, Subject: {self.house}"
    
class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        
    def __str__(self):
        return f"Professor: {self.name}, Subject: {self.subject}"
        
wizard = Wizard("JRomero")       
student = Student("Jc","Slytherin")
professor = Professor("Romero","Defense Against Dark Arts")

print(wizard)
print(student)
print(professor)
#para mostrar los valores de las instancias de tus clases en el terminal definir el método __str__