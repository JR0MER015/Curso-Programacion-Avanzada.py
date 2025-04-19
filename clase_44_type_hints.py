#Type hints, 
#mypy , pip install mypy
#verificar si las variables usan el typo correcto

#def meow(n):
#    for _ in range(n):
#        print("meow")
        
#number = input("Number: ")
#meow(number)

#TypeError: 'str' object cannot be interpreted as an integer

#def meow(n:int):#especificando que lo que operare sera un integro, es una pista de que n debe ser un int
#    for _ in range(n):
#        print("meow")
        
#number = input("Number: ")
#meow(number)

#el error sigue pero podria usar mypy en el terminal y me dira que es 
#instalar mypy ya que no lo tengo

#def meow(n:int):
#    for _ in range(n):
#        print("meow")
        
#number: int = int(input("Number: "))#es una buena costumbre definir el tipo de dato que quiero ingresar
#meow(number)

#def meow(n:int) -> None:# el valor de retorno es ninguno por eso lo menciono como  None
#    for _ in range(n):
#        print("meow")
        
#number: int = int(input("Number: "))
#neows:str = meow(number)
#meow(number)

def meow(n:int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows:str = meow(number)
print(meows, end="")










