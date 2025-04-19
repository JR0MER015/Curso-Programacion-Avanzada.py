#operator overloading
#aqui un símbolo no necesariamente tiene que significar lo que yo quiero el ejemplo + ya que puede concatenar o sumar o solo ser el símbolo

#representando la bobeda de un banco de magos , galleons,sickles,knuts son monedas de harry potter y cuyos valores por defecto seran 0 
#class Vault:
#    def __init__(self,galleons=0, sickles=0, knuts=0):
#        self.galleons = galleons
#        self.sickles = sickles
#        self.knuts = knuts
        
#    def __str__(self):
#        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    
#potter = Vault(100,50,25)

#print(potter)

#weasley = Vault(25,50,100)
#print(weasley)

#total = potter + weasley# esto no se puede ya que lo devuelvo es un string debo hacerlo accediendo a la clase, pero lo puedo hacer con sobrecarga de operaciones, para evitar todo lo de abajo
#galleons = potter.galleons + weasley.galleons
#sickles = potter.sickles + weasley.sickles
#knuts = potter.knuts + weasley.knuts

#total = Vault(galleons,sickles,knuts)
#print(total)
        
#usando el operador de sobrecarga para evitar tantas suma aritmetica del código de arriba
class Vault:
    def __init__(self,galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    #sobrecargando para que me devuelva el valor total
    def __add__(self,other):#significa añadir cualquier other 
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons,sickles,knuts)
        
       
potter = Vault(100,50,25)

print(potter)

weasley = Vault(25,50,100)
print(weasley)

total = potter + weasley
print(total)


#revisar la lista de operadores sobrecargados ,estan en especial-methods-names     