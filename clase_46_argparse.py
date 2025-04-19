#import sys 

#if len(sys.argv)==1:
#    print("Meow")
#else:
#    print("usage: meow.py")
    
#cuando corro el programa como la el valor de la dirección es 1 me muestra 
#PS C:\Users\jcrom\Desktop\Python> & C:/Users/jcrom/AppData/Local/Programs/Python/Python312/python.exe c:/Users/jcrom/Desktop/Python/curso_edutin_programacion_avanzada.py/clase_46_argparse.py
#Meow
#ahora si uso algo como
#C:/Users/jcrom/AppData/Local/Programs/Python/Python312/python.exe c:/Users/jcrom/Desktop/Python/curso_edutin_programacion_avanzada.py/clase_46_argparse.py 3
#regresa
#usage: meow.py

#tambien podemos usar bandera para que especifiquen el número de veces que se quiero que algo se ejecute en el terminal, esto puede ser mediante el código -n3, especifica el número de veces que se quiere ejecutar desde la línea de comando
#PS C:\Users\jcrom\Desktop\Python> C:/Users/jcrom/AppData/Local/Programs/Python/Python312/python.exe c:/Users/jcrom/Desktop/Python/curso_edutin_programacion_avanzada.py/clase_46_argparse.py -n3

#import sys 

#if len(sys.argv)==1:
#    print("Meow")
#elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#    n = int(sys.argv[2])
#    for _ in range(n):
#        print("Meow")    
#else:
#    print("usage: meow.py")
    
 #PS C:\Users\jcrom\Desktop\Python> C:/Users/jcrom/AppData/Local/Programs/Python/Python312/python.exe c:/Users/jcrom/Desktop/Python/curso_edutin_programacion_avanzada.py/clase_46_argparse.py -n 3
 #asi se imprime 3 veces   
    
    
#una biblioteca que ayuda es ARGPARSE,cuando se quiere usar determinada configuracion en la línea de comando , ejemplo si el usuario ingresa -a o -p en vez de -n.

    
import argparse #analisador de arguentos

parser = argparse.ArgumentParser()
parser.add_argument("-n")

arg = parser.parse_args()#analisa todos los argumentos de la linea de comandos 

