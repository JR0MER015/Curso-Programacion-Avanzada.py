#estos códigos que he usado son buenos pero limitados ya que si quiero añadir más cosas 
#una clase es plano para piesas de datos para asignar valores
#las clases permiter crear nuestros propios objetos

#class Student:
#    ...#estos puntos significa que no he definido nada más por ahora lo que se quiere es probar sus objetos en la función get_student

#def main():
#    student = get_student()   
#    print(f"{student.name} is from {student.house}")#uso de comillas simples y dobles
      
    
#def get_student():
#    student = Student()#creando objetos desde la clase
#    student.name = input("Name: ").strip().title()#atributos
#    student.house = input("House: ").strip().title()#atributos 
#    return student
    
    
#if __name__ == "__main__":
#    main()
    
#las clases son mutables y puedes hacerlos inmutables , en este caso los atributos son nombre y casa

class Student:
    ...#estos puntos significa que no he definido nada más por ahora lo que se quiere es probar sus objetos en la función get_student

def main():
    student = get_student()   
    print(f"{student.name} is from {student.house}")#uso de comillas simples y dobles
      
    
def get_student():
    name = input("Name: ").strip().title()#atributos
    house = input("House: ").strip().title()#atributos
    student = Student(name,house) 
    return student
    #asiendo el código más eficiente validando los el ingreso de datos.
    
if __name__ == "__main__":
    main()