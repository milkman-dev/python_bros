

def funcion():
    x = float(input("Escribe un número"))
    y = float(input("Escribe un número"))

    if x+y<100:
        w = x / y
        print(w)
    else:
        w = x + y
        print(w)
    return w

funcion()


lista = [0,1,2,3,4,5,6,7,8,9]

print(lista[2])

lista.append(10) # agregar elementos
print(lista)


#dictionary tienen propiedad llave y valor
diccionario = {1:"uno",2:"dos",3:[1,2,3]}  # las llaves deben de ser del mismo tipo simempre (pero pueden ser de cualquier tipo)

print(diccionario[3])


#loops   for loop

for i in lista:
    print(i)



#listas dos dimensiones

lista2d = [["A","B","C","D",""],[24,23,22,21,0,0,0,0,0,0,0,0,0,0,0,0],[True,True,True,True,True,True,True]]

print(lista2d[0][1])