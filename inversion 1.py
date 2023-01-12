""" Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión."""

Invierte=int(input("hola biemvenido introdusca la cantidad a invertir: "))
InteresA=float(input("ingrese el interes anual: "))
Años=int(input("ingrese la cantidad de años que desea invertirlo: "))

print("Capital final despues de ",Años,"de inversion es de: ", (Invierte* (InteresA / 100 + 1) ** Años, 2))