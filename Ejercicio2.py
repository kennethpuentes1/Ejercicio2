texto_1= "Hola compañeros" *4 
texto_2= "Que tal "  
texto_3= "Que tal la vida?"
texto_4= "Hola "
texto_4 +=" "
texto_4 += "Que tal?"
texto_5="Hola Brother"
texto_5a= texto_5.find("Bro")
texto_6="HOLA A TODOS"
texto_6a=texto_6.lower()
texto_7="hola a todos"
texto_7a=texto_7.upper()
texto_8="oso osado"
texto_8a= texto_8.replace("o", "Casa")
texto_9="La carretera es peligrosa"
texto_9a= texto_9[4:20]
texto_10=["El", "Colegio", "es" , "aburrido"]
texto_10a=["Menos mal", "Ya estoy en la universidad."]
texto_10.insert(0,texto_10a)
texto_11=["Que", "Aburrimiento", "Leer", "Sobre", "Huevos"]
nums=[1, 6, 4, 7, 9, 2]
sorted_texto_11= sorted(texto_11)

print(texto_1 + texto_2) 
print(texto_10)
print(texto_4)
print(len(texto_3))
print(texto_5a)
print(texto_6a)
print(texto_7a)
print(texto_8a)
print(texto_9a)
print(texto_10a)
print(sorted_texto_11)