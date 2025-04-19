#Global, variable globales o locales 
#balance = 0

#def main():
#    print("Balance:",balance)
#    deposit(100)
#    withdraw(50)
#    print("Balance:",balance)
    
#def deposit(n):
#    balance += n
    
#def withdraw(n):
#    balance -= n      
    
#if __name__ == "__main__":
#    main()
    
#UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value
#en el caso anterior la variable global no se modifica por las variables locales por eso se usa global
   
#balance = 0

#def main():
#    print("Balance:",balance)
#    deposit(100)
#    withdraw(50)
#    print("Balance:",balance)
    
#def deposit(n):
#    global balance #globar lo que hace es decirle a Pytho que utilice varibles globales y locales 
#    balance += n
    
#def withdraw(n):
#    global balance
#    balance -= n      
    
#if __name__ == "__main__":
#    main()
    
#podemos mejorar este código usando POO :

class Account:
    def __init__(self):
        self._balance = 0 # el balance es privado
        
    @property#variable de instancias que se pueda leer o escribir es un getter
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance += n
        
    def withdraw(self,n):
        self._balance -= n
        
def main():
    account = Account()
    print("Balance:",account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:",account.balance)


if __name__ == "__main__":
    main()
    