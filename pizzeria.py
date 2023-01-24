"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles 
para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""

print("bienvenido a la pizzeria napoli")

tipo_pizza=input("para una pizza vegetariana ponga v para una regular ponga r: ")[:1]

if tipo_pizza == str("v"):
    print("los ingredientes vegetarianos son pimiento y tofu")
    ingredientes=input("ingrese p para pimiento o t para tofu")[:1]
    if ingredientes==str("t"):
        print("su pizza es vegetarian y el ingredient es tofu")
    elif ingredientes==str("p"):
        print("su pizza es vegetarian y el ingredient es pimiento")
        
    


elif tipo_pizza==str("r"):
    print("los ingredientes regulares son peperoni,jamon y salmon")
    
    ingredientesr=input("ingrese p para peperoni , j para jamon o s salmon")[:1]
    if ingredientesr==str("p"):
        print("su pizza es regular y el ingredient es peperoni")
    elif ingredientesr==str("j"):
        print("su pizza es regular y el ingredient es jamon")
    elif ingredientesr==str("s"):
        print("su pizza es regular y el ingredient es salmon")

else:
    print("codigo invalido")

