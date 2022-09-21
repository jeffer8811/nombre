lista =["pan", "leche", "azucar"]
lista.append("maíz")
lista.pop(-1)
lista.sort()
lista.reverse()
lista.remove("pan")

print(lista)



tuple=("uno","dos","tre","cuatro","cuatro")
tuple.count("uno","dos","tre","cuatro","cuatro")





# from importlib import import_module
# from re import I
# from tkinter import Y


# for num in range(10):
#     if num%2 == 0:
#         print("numero par" ,num)
#     else:
#         print("Numero impar",num)
# lista = []
# Y = input("ingresa el producto")
# lista.append(Y) 
# print(lista)       


# lista = []
# x = int(input("cantidad de productos"))
# for i in range(x):
#     x = input("ingresa el producto")
#     lista.append(x)
# print(lista)

# from re import U, X
# from tkinter import Y


# Y = {
#     "nombre": [],
#     "cantidad": []
# }

# U = input ("Ingrese el producto")
# X =  int(input("Ingrese el cantidad"))

# Y["nombre"].append(U)
# Y["cantidad"].append(X)

# print(Y)

# cant=0
# while cant<5:
#     print("hola mundo")
# #     cant += 1
# from ast import Num
# from cgi import print_arguments

num1=int(input("introduce el primer numero"))
num2=int(input("introduce el segundo numero"))
opcion= 0 
while True:
    print("""
    opciones:
    1) Suma
    2) resta
    3) multiplicaión
    """)
    opcion=int(input("ingrese la operacion a realizar"))

    if opcion == 1:
        print("La suma es:", num1 + num2)
        print("deceas realizar otra operacion?")
        rpta=input()
        if rpta=="s":
            continue
        else:
            break
    elif opcion == 2:
        print("la resta es:", num1 - num2)
        rpta=input()
    elif opcion == 3:
        print("la multiplicasion:", num1 * num2)
        
        
        
        
        cant=0
while cant<5:
    print("hola mundo")
    cant += 1

