#un diccionario son claves y valores y tienen una mejor semantica para su lectura

#def main():
#    student = get_student()
#    if student[0] == "Padma":
#        student[1]= "Ravenclaw"#
#    print(f"{student[0]} is from {student[1]}")   
    
#def get_student():
#    name = input("Name: ").strip().title()
#    house = input("House: ").strip().title()
#    return [name,house]#ahora es una lista y si es mutable

#if __name__ == "__main__":
#    main()
    
#ahora transformare esto en un diccionario

#def main():
#    student = get_student()
    #if student[0] == "Padma":#esta validacion es de lista no aplica a diccinarios
    #    student[1]= "Ravenclaw"#
    #print(f"{student["name"]} is from {student["house"]}")#problema al usar comillas dobles y sencillas 
#    print(f"{student['name']} is from {student['house']}")#uso de comillas simples y dobles
      
    
#def get_student():
#    student = {}#aqui creo el diccionario vacío
#    student["name"] = input("Name: ").strip().title()#aqui ya esta definida la clave = valor
#    student["house"] = input("House: ").strip().title()
#    return student    

#if __name__ == "__main__":
#    main()
    
#otra forma en la que puedo modificar el diccionario seria creandolo ya con valores antes de que este vacío

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} is from {student['house']}")#uso de comillas simples y dobles
      
    
def get_student():
    name = input("Name: ").strip().title()#variables que se añadiran al diccionario
    house = input("House: ").strip().title()
    return {"name": name, "house": house}   

if __name__ == "__main__":
    main()
    