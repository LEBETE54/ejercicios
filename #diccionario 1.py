#diccionario 1
"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario. """
divisas={"dollar":"$","yen":"¥","euro":"€"}
moneda=input("escribe el nombre de la divisa que deseas y se te mostrara su simbolo: ")
if moneda.title() in divisas:
   print(moneda[divisas.title()])
else:
    print("la divisa no esta disponible")
   