#escribir código para probar mis programas 

#probando el código del archivo clase_3_def2.py , que calcula el cuadrado de un número

from clase_3_def2 import cuadrado

#creo una función para probar un cuadrado
def main():
    print("Ejecutando main()")
    test_cuadrado()


def test_cuadrado():
    assert cuadrado(2) == 4
    assert cuadrado(3) == 9

#def test_cuadrado():
#    if cuadrado(2) != 4 :
#        print("2 al cuadrado no era 4")
#    if cuadrado(3) != 9:
#        print("3 al cuadrado no era 9")
        

    
if __name__ == "__main__":
    main() 

#esto da un error  AssertionError   
#herramienta para probar codigos pytest ,biblioteca de tercero
#pruebas unitarias son pruebas para funciones
#pip install pytest
#para probarlo pytest se ejecuta en el terminal

   
