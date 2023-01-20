#condicionales 2

"""Para tributar un determinado impuesto se debe ser mayor de 16 años
y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
y muestre por pantalla si el usuario tiene que tributar o no."""


edad=int(input("introdusca su edad: "))

ingresos= float(input("introdusca sus ingresos mensuales totales: "))

if edad>=16 and ingresos>=1000:
    print("usted es valido para tributar: ")
else:
    print("afortunadamente usted todavia no tributa")