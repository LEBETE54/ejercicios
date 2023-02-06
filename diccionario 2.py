"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""

nombre=input("ingresa tu nombre: ")
edad=input("ingresa tu edad: ")
direccion=input("ingresa tu direccion: ")
telefono=("ingresa tu telefono: ")
#aqui generamos el diccionario de la persona
persona={"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}

print(persona["nombre"],"tiene",persona["edad"],"vive en ",persona["direccion"]," y su telefono es ",persona["telefono"])