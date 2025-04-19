#importando funciones desde saying.py 

import sys
from saying import hello,goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1]) #ahora como ya cree el constructor en saying no imprime main(), si no solo hello
    
if len(sys.argv) == 2:
    goodbye(sys.argv[1])#probando decir adios
    
    