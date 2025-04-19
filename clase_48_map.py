#MAP 

#def main():
#    yell("This is Sparta")
    
#def yell(phrase):
#    print(phrase.upper())
    
#if __name__ == "__main__":
#    main()
    
#ahora podemos probar que pasa si usamos una lista 
#def main():
#    yell(["This","is", "Sparta"])
    
#def yell(words):
#    uppercased = []
#    for word in words:
#        uppercased.append(word.upper())
#    print(uppercased, end="")
    
#if __name__ == "__main__":
#    main()

#['THIS', 'IS', 'SPARTA'], asi se muestra
#pero para sacarlas puedo usar * en el print
#def main():
#    yell(["This","is", "Sparta"])
    
#def yell(words):
#    uppercased = []
#    for word in words:
#        uppercased.append(word.upper())
#    print(*uppercased, end="")#aqui estoy desempaquetando
    
#if __name__ == "__main__":
#    main()
#THIS IS SPARTA

#mejorando el código
#def main():
#    yell("This","is", "Sparta")
    
#def yell(*args):#*args que sean variables los argumentos que voy a ingresar
#    uppercased = []
#    for word in args:#itero sobre el argumento
#        uppercased.append(word.upper())
#    print(*uppercased, end="")#aqui estoy desempaquetando
    
#if __name__ == "__main__":
#    main()

#tambien puedo hacer esto
#def main():
#    yell("This","is", "Sparta")
    
#def yell(*words):#*args con el nombre del argumento
#    uppercased = []
#    for word in words:#itero sobre el argumento
#        uppercased.append(word.upper())
#    print(*uppercased, end="")#aqui estoy desempaquetando
    
#if __name__ == "__main__":
#    main()
    
#Map , es una función en pytho que te permite mapear el código
def main():
    yell("This","is", "Sparta")
    
def yell(*words):
    uppercased = map(str.upper,words)#le estoy pasando la función upper a map ,sobre los args words, y lo que hace es iterar sobre ellos .,devuelve una lista y el código es más apretado
    print(*uppercased, end="")
    
if __name__ == "__main__":
    main()