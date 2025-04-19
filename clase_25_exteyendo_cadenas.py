#pediremos información a un usurio mediante una URL
#el objetivo sera obtener el nombre de usuario de una URL

#url = input("URL: ").strip()
#print(url)

#creamos una nueva variable la cual validara el username
#url = input("URL: ").strip()

#username = url.replace("https://twitter.com//", "")#remplaza lo que quiero, el primero campo es lo que remplazo y lo segundo es con que lo remplazo

#print(f"Username= {username}")

#el problema que replace busca exactamente lo que remplazo y con eso permite que el usuario ingrese cualquier cosa, por eso vamos a usar otra función
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com//")#esta función elimina prefijos que son cadenas por lo cual no necesito un nuevo argumento para remplazarla

print(f"Username= {username}")
