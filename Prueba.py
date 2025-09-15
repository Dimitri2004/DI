"""Colecciones

    Listas

    Tuplas

    Diccionarios

"""
#Listas
l=[23, 4.20, 16-3j, "albatros", -5, 22,[34,"Manuel"],4>>1,~5]
print(type(l))


l[4]= "marcelo"
l[6]=[1,2,3,4]

print(l[6][-3])#puedes hacer que empiece por la derecha con - delante del nombre de la lista

#Partidas
print(l[2:5])
print(l[4][1:3])
print(l[:-3])
print(l[1:5:2])
print(l[::-1])

#Tuplas

t=(2,5,2+3j, "Alberto",[1,3,4,5,6],6,9) #Elementos inmutables dentro de la tupla
t[4][3]=2
print(t)