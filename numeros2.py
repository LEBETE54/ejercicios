"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
    donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
    (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato 
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
    """

#usaremos los rangos para este ejemplo

tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])
#aqui le especificamos al programa el rango de carateresd que queremos que imprima