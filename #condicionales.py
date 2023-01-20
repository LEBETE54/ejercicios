#condicionales

"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida p
or el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""
#se usa lower para transformar todos los caracteres a minusculas
contra=("contraseña: ")

verification=input("introdusca su contraseña nuevamente: ")

if contra ==verification.lower():
    print("la contraseña es correcta")
else:
    print("la contra seña es erronea")
