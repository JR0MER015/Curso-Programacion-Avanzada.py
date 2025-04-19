def main():
    hello("World")
    goodbye("World")
    
def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Good bye, {name}")
    
#main()#si lo dejo a si cuando lo use en otra función tendre problemas ya que python me leera todas las funciones
#ya que esta en main(), para selecionar lo que quiero usare la la sigiente funcion con el contructor__

if __name__ == "__main__":#la variable __name__ es especial,nombre no se establece como principal
    #se establece como un paquete interno por el constructor
    main()