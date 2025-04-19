#comprehensions dict

#students = ["Hermione","Harry","Ron"]

#gryffindors = []

#for student in students:
#    gryffindors.append({"name":student, "house":"Gryffindor"})

#print(gryffindors)

#mejorando el código para que este mas comprimido y claro
#students = ["Hermione","Harry","Ron"]

#gryffindors = [{"name":student,"house":"Gryffindor"} for student in students]

#print(gryffindors)

#[{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]

#mejorando el codigo
students = ["Hermione","Harry","Ron"]

gryffindors = {student:"Gryffindor" for student in students}

print(gryffindors)

#creando un diccioario key:value y lo lleno con la iteracion de for :
#{'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}

