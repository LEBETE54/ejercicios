"""Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida."""

#Para invertir una cadena de texto (string) en Python, puede utilizar el método de slicing con un paso negativo.
original_strig=str(input("introduzca una frase: "))
string_inver=original_strig[::-1]
print(string_inver)

#También puede utilizar el método "reverse()" de las listas:

original_string = "Hello World"
list_string = list(original_string)
list_string.reverse()
inverted_string = "".join(list_string)
print(inverted_string)
#el resultado es el mismo solo que aqui convertimos el str en una lista y luego la invertimos