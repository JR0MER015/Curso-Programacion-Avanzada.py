#Enumerate

#students = ["Hermione","Harry","Ron"]

#for student in students:
#    print(student)

#eso esta bien pero no veo ningun rango númerico que me diga cual es el primero , segundo o tercero
#students = ["Hermione","Harry","Ron"]

#for i in range(len(students)):
#    print(i, students[i])


#el problema es que los enumera desde 0 para eso hacer lo siguiente
#students = ["Hermione","Harry","Ron"]

#for i in range(len(students)):
#    print(i+1, students[i])
    
#pero hay una función que me ayuda a esto de forma más facil que es enumerate
# enumerate(iterable, start = 0)

students = ["Hermione","Harry","Ron"]

for i, student in enumerate(students):
    print(i + 1 , student)

#esto itera y genera un retorno en orden
#1 Hermione
#2 Harry
#3 Ron


