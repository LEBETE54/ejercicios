""" Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE>
tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre."""

Nombre=str(input("esriba su nombre: "))
#aqui usamos len para imprimir la longitud de la variable osea la cantidad de espacios que posee no confundir esto con la posicion que se cuenta desde el 0
print(Nombre ,"tiene",len(Nombre))