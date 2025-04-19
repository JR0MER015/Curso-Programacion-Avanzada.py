#list comprehensions
#def main():
#    yell("This","is", "Sparta")
    
#def yell(*words):
#    uppercased = map(str.upper,words)#le estoy pasando la función upper a map ,sobre los args words, y lo que hace es iterar sobre ellos .,devuelve una lista y el código es más apretado
#    print(*uppercased, end="")
    
#if __name__ == "__main__":
#    main()
    
#comprimir la una lísta pero sin usar map
#def main():
#    yell("This","is", "Sparta")
    
#def yell(*words):
#    uppercased = [word.upper() for word in words] #esto es pythonico
#    print(*uppercased, end="")
    
#if __name__ == "__main__":
#    main()
    
#THIS IS SPARTA

#*****************************************************************************+
#realizando otro ejemplo

students = [
    {"name":"Hermione","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Drako","house":"Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
    
#iterando de foma mas pythonica un diccionario