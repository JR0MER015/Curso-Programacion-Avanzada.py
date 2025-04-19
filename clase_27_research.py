#import re

#url = input("URL:").strip()

#matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)#primero tengo la string ,luego lo que voy a buscar que es la url y al final la validación para ignorara las mayúsculas
#if matches:
#    print(f"Username:",matches.group(2))
    
#mejorando el codigo usando el walrus
#import re

#url = input("URL:").strip()
#if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#    print(f"Username:",matches.group(2))
    
#usando la función (?...) que esta en re.search , para non-capturing
#import re

#url = input("URL:").strip()
#if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):#(?:www\.) con esto digo que no capture este grupo , y ademas el ? fuera dice que es opcional(?:)
#    print(f"Username:",matches.group(1))
    
#modificando un como mas el código
#import re

#url = input("URL:").strip()

#if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([\w]+)$", url, re.IGNORECASE):
#    print(f"Username:",matches.group(1))
    
#https://twitter.com/jromero

#probando que acepta .com,.es,.etc
import re

url = input("URL:").strip()

#if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|es|net|org)/([\w]+)$", url, re.IGNORECASE):
    print(f"Username:",matches.group(1))
    
#https://twitter.es/jromero

#re.split(pattern, strings, maxsplit = 0, flags = 0), usada para dividir expresiones regulares
#re.findall(pattern, strings, flags=0) , se utiliza para encontrar todas las coinsidencias 