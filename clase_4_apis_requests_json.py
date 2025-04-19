#una APIs es una interfaz de  programación aplicaciones 
#permite acceder a información de terceros 
#libreria requests te permite hacer peticiones web 
#automizo documentación para optener información de paginas web http o https
# pip isntall requests
# itunes.py # apple tiene su propia APIs para su servicio de Itunes para descargar información 

#json , es java scrip on notation
#esto se descarga desde la pagina web de la de donde quiero adquirir información 
#es un archivo de texto, si lo reviso es un patron en java, y son clave valor 
import json #esta ya esta instalada en python 
import requests #peticiones http
import sys #argumentos de lineas de comando

#ahora ingreso unsa comprobación para ver la longitud
if len(sys.argv) != 2: #nombre del archivo y banda
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])#se concstena 
#y busca lo que quiero en el terminal , lo que esta arriba es el JSON , aqui en limit= puedo poner x número
#El nombre de la banda va en mayúscula

#print(response.json())
#al imprimir esto no se ve bien ya que no tiene un formato amigable pero  hay una libreria Json que 
#lo hace mas amigable
#hay que instalar JSON

#usando la libreria json 
#print(json.dumps(response.json()))# json.dumps es para hacer el volcado y que se vea bien

#print(json.dumps(response.json(), indent = 2))#es lo mismo pero con la sangria indent
#al imprimir esto ya se muestra el Json en una forma mas leible y se muestra el diccionario
#se muestra las claves por las cuales podria llamarlo o iterarlo

#como ya se la clave ahora lo que hago es iterarlo para que se muestre la llamada
 
o = response.json()#creo una variable para llamr al json 
#ahora itero la variable
for result in o["results"]:
    print(result["trackName"])#trackName lo obtuve al print con indent 2


