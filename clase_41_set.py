#etcetera 
#todo lo ademas que puedes hacer con python
#set es un cónjunto, elímina los duplicados

students = [
    {"name": "Hermione","house": "Gryffindor"},
    {"name": "Harry","house":"Gryffindor"},
    {"name": "Ron","house":"Gryffindor"},
    {"name": "Draco","house":"Slytherin"},
    {"name": "Padma","house":"Ravenclaw"},
]

#houses = []
#for student in students:
#    if student["house"] not in houses:
#        houses.append(student["house"])
        
#for house in sorted(houses):
#    print(houses)

#el problema con ese código es que estoy usando una lista y me devolvera duplicados , es mejor usando un conjunto y asi elímino los duplicados.


houses = set() #se crea el conjunto
for student in students:
    houses.add(student["house"])
        
for house in sorted(houses):
    print(houses)


