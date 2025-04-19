#command- line arguments
#argumentos de línea de comandos SYS
#módulo sys y argv( argumentos de vectores)
#import sys

#print("Hello,my name is", sys.argv[1])#inicia de 1 ya que 0 es el nombre del programa

#el error IndexError , significa que estoy llamando un valor que esta fuera de rango 
#es decir que el valor puede que tenga un valor menor al que estoy llamando

#commo no se sabe si puede haber o no un valor en la terminal creare una excepción 
#import sys

#try:
#    print("Hello,my name is", sys.argv[1])
#except IndexError:
#   print("Too few arguments")

#haciendo mas fino el programa
#import sys

#if len(sys.argv) < 2:
#    print("Too few arguments")
#elif len(sys.argv) > 2:
#    print("Too many arguments")
#else:
#    print("Hello,my name is", sys.argv[1])
    
#si yo hago esto me da error de nombre
#import sys

#if len(sys.argv) < 2:
#    print("Too few arguments")
#elif len(sys.argv) > 2:
#    print("Too many arguments")

#print("Hello,my name is", sys.argv[1]) da error ya que no esta anidado y asumo que el valor esta entre 1

#para mejorar eso lo que hago es usar el valor 

#import sys

#if len(sys.argv) < 2:
#    sys.exit("Too few arguments")#sys.exit es una funcion de sys que me saca del sistema si no cumplo una condicion
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")
    
#print("Hello,my name is", sys.argv[1])

#para usar esta funcion llamo a la dirección asi:
# & C:/Users/jcrom/AppData/Local/Programs/Python/Python312/python.exe c:/Users/jcrom/Desktop/Python/curso_edutin_programacion_avanzada.py/name.py Juan

#mejorando el programa para que no cuente el limite de caracter maximos
#import sys

#if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
    
#voy a iterar para cada argumento que este en la terminal
#for arg in sys.argv:
#    print("Hello,my name is", arg)#la variable arg puede llamarse de cualquier forma
#el problema es es que la impresión inicia con el nombre del programa y eso hay que arreglarlo

    
#import sys

#if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
    
#for arg in sys.argv:
#    print("Hello,my name is", arg)


#usando slices para que la iteracion y la impreción comience desde 1 y no desde 0

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    
for arg in sys.argv[1:]:#incluyo en la lista los parametros del rango de impreción
                #si [1:-1] el -1 eliminaria mi ultimo dato el del final ya que cuenta al reves
    print("Hello,my name is", arg)

#los paquetes son bibliotecas de terceros que podemos instalar en nuestra propias librerias o programas
#donde coseguir paquetes en la pagina PyPI o en la pagina pypi.org
#PIP es la paqueteria de python y puedo instalarla y ya tengo almo más en python 





