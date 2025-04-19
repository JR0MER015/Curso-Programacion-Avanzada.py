#filter , filtro con otro enfoque

students = [
    {"name":"Hermione","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Drako","house":"Slytherin"},
]


#solo que esto es muy verboso asi que hay que usar algo más pythonico
#def is_gryffindor(s):
#    if s["house"] == "Gryffindor":
#        return True
#    else:
#        return False

#esta función es tomada en el código de filter de manera más pythonica
#def is_gryffindor(s):
#    return s["house"] == "Gryffindor"

#lambda función que solo utilizare una vez
gryffindors = filter(lambda s:s["house"] == "Gryffindor",students)

for gryffindor in sorted(gryffindors, key=lambda s:s["name"]):
    #print(gryffindor)
    print(gryffindor["name"])
    