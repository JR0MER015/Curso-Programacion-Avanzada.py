#los paquetes son bibliotecas de terceros que podemos instalar en nuestra propias librerias o programas
#donde coseguir paquetes en la pagina PyPI o en la pagina pypi.org
#PIP es la paqueteria de python y puedo instalarla y ya tengo almo más en python 

#puedo usar pip list para ver que paquetes tengo instalados y trabajar con ellos 
#hauseofgabe instalar cowsay

#sys.argv ayuda a automatizar procesos una vez ya estemos comodos 

import cowsay# esta paqueteria no esta instalada
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])#para concatenar uso + y la forma depende de la paqueteria
    #uso la lista de rango 1 ya que cero es el nombre del paquete y y 1 es mi nombre 
    # lo que muestra es arte ACI

#el paquete cowsay tiene otras funciones como trex
#import cowsay# esta paqueteria no esta instalada
#import sys

#if len(sys.argv) == 2:
    #cowsay.trex("Hello, " + sys.argv[1])#investigar mas de cowsay para ver mas animales
    #cowsay.trex("Hello, " + sys.argv[1])
