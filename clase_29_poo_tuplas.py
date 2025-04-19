def main():
    name, house = get_student()
    print(f"{name} is from {house}")   
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name,house #siempre que se usa , para devolver 2 variables devuelve una tupla tambien le puedo poner ()

if __name__ == "__main__":
    main()
    
#ajustando el código para que el desempaquetado se realice dentro de una variable y asu vez la tupla semuestre mas facilmente al lector,recuerda que las tuplas son inmutables

#def main():
#    student = get_student()
#    print(f"{student[0]} is from {student[1]}")   
    
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return (name,house)#es lo mismo que las comas ,  pero para que se entienda mas la tupla

#if __name__ == "__main__":
#    main()

#creando una validacición para nombres existentes y sus casas
#def main():
#    student = get_student()
#    if student[0] == "Padma":
#        student[1]= "Ravenclaw"#da TypeError ya que las tuplas no se pueden modificar 
#    print(f"{student[0]} is from {student[1]}")   
    
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return (name,house)#es lo mismo que las comas ,  pero para que se entienda mas la tupla

#if __name__ == "__main__":
#    main()
    
#si lo que quiero es modificar y que alguien más use mi código uso las listas 
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1]= "Ravenclaw"#
    print(f"{student[0]} is from {student[1]}")   
    
def get_student():
    name = input("Name: ").strip().title()
    house = input("House: ").strip().title()
    return [name,house]#ahora es una lista y si es mutable

if __name__ == "__main__":
    main()