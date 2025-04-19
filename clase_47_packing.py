#pack and unpack
#first, _ = input("What is your name?: ").split(" ")
#print(f"hello, {first}")

#def total(galleons, sickles,knuts):
#    return (galleons * 17 + sickles ) * 29 + knuts

#print(total(100,50,25), "Knuts")

#modificando el código
#def total(galleons, sickles,knuts):
#    return (galleons * 17 + sickles ) * 29 + knuts

#coins = [100,50,25]

#print(total(coins[0],coins[1],coins[2]), "Knuts")

#probando un unpacking
#def total(galleons, sickles,knuts):
#    return (galleons * 17 + sickles ) * 29 + knuts

#coins = [100,50,25]

#print(total(*coins), "Knuts")#para desempacar tambien podemos usar *X, *variable desempaquetara todo lo de la variable

#realizando otras pruebas 
#def total(galleons, sickles,knuts):
#    return (galleons * 17 + sickles ) * 29 + knuts

#print(total(galleons = 100,sickles = 50,knuts =25), "Knuts")

#como tengo un valor clave valor puedo usar un diccionario
#def total(galleons, sickles,knuts):
#    return (galleons * 17 + sickles ) * 29 + knuts

#coins = {"galleons":100, "sickles":50,"knuts":25}

#print(total(coins["galleons"],coins["sickles"],coins["knuts"]), "Knuts")

#mejorando el código para que se desempaque mejor
#def total(galleons, sickles,knuts):
#    return (galleons * 17 + sickles ) * 29 + knuts

#coins = {"galleons":100, "sickles":50,"knuts":25}

#print(total(**coins), "Knuts")#para diccionarios uso 2** 

#mejorando el código para que tenga valores pot defectos 
#def total(galleons=0, sickles=0,knuts=0):
#    return (galleons * 17 + sickles ) * 29 + knuts

#coins = {"galleons":100, "sickles":50,"knuts":25}

#print(total(**coins), "Knuts")

#*ARGS devuelve tuplas ,**ARGS devuelve diccionarios

#def total(galleons=0, sickles=0,knuts=0):
#    return (galleons * 17 + sickles ) * 29 + knuts

#coins = {"galleons":100, "sickles":50,"knuts":25}

#print(total(**coins), "Knuts")

#vamos a crear una función que tome argumentos variables
#def f(*args, **kwargs):
#    print("Positional:",args,kwargs)
      
#f()
#esto lo que muestra es 
#C:/Users/jcrom/AppData/Local/Programs/Python/Python312/python.exe c:/Users/jcrom/Desktop/Python/curso_edutin_programacion_avanzada.py/clase_47_packing.py
#Positional: () {}
#f(1,2,3,4)
#Positional: (1, 2, 3, 4) {}
def f(*args, **kwargs):
    print("Positional:",kwargs)

f(a=100,b=20,c=25)
#Positional: {'a': 100, 'b': 20, 'c': 25}
    




