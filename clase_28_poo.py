#crear un programa que pida a un usuario su nombre , casa y de donde es etc ?

#name= input("Name: ")
#house= input("House: ")
#print(f"{name} is from {house}")

#con esto ya  tengo la lógica principal para un código que puede atender más problemas ahora con esto puedo crear una función 

#def main():
#    name= input("Name: ")#aqui voy asumir que tengo una función get_name
#    house= input("House: ")#aqui una función get_house
#    print(f"{name} is from {house}")
    
#por lo cual el código se veria asi
#def main():
#    name= get_name()#aqui voy asumir que tengo una función get_name
#    house= get_house()#aqui una función get_house
#    print(f"{name} is from {house}")   
    
#def get_name():
#    name = input("Name: ")#puedo apretar el código asi : return input("Name: ")
#    return name

#def get_house():
#    house = input("House: ")
#    return house

#tambien creo el habito constructor para que pueda ser llamado mas adelantepor otra persona

#if __name__ == "__main__":
#    main()
    
#pero puedo mejorar el código tomando los valores des una función llamada estudiante y que me verifique los valores que estoy ingresando

#por lo cual el código se veria asi
def main():
    name, house = get_student()
    print(f"{name} is from {house}")   
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name,house

if __name__ == "__main__":
    main()
