"""Colecciones

    Listas

    Tuplas

    Diccionarios

"""
from pkg_resources import yield_lines

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
t2=5,
print(type(t2)) #Es posible su salida de diferentes formas sin cambiar su contenido

#Condiciones

numeros=[1,2,3,4,5,20,45,67,3,4,5,6,7,8]
for numeros in range(5):
    print(numeros)


"""for indice in range(3,10,3):
    print(numeros[indice])
    """


#Diccionarios
d={1: "uno",2:"dos",3:"tres"}#diccionario

print(d[3])

l2=[1,2,3]#lista
l3=list((1,2,3))#tupla

t2=[1,2,3]
t3=tuple(l3)#Se puede crear tupla con listas
l3[0]=1000
print(t3)
print(t3,l3)

d2={1:"1",2:"11",3:"111"}
d3=dict()#diccionario vacio

l2.append([3,2,1])#inserta el objeto en lista como único elemento
l2.extend([3,2,(2,"Dos","11"),1])#añade como elementos a la lista
l2.insert(3,"Objeto en 4ª lugar")#añade en el lugar el objeto descrito

print(l2.count(3))#busca el elemento y lo cuenta las veces en q se repita

print(l2.index(3,3,7))#busca coincidencias a partir del inicio y fin de la lista
extraer=l2.pop(5)#Quita el valor de la lista en la posicion asignada
l2.remove(3)#elimina la primera coincidencia de la lista
l2.reverse()#invirte la lista
t3=l2[::-1]#la devuelve desinvirtiendola
print("Elemento extraido :",extraer)
print(l2)
print(t3)
l4=[3,4,6,10,45,8]
#print(l2.sort(reverse=True))#ordena listas de manera inversa

l5=["un","dos","tres","cuatro","cinco"]
l5.sort(key=len)#ordena por tamaño de frase
print(l5)
tabla_alturas=[("Manuel",1.17),("Pepe",2.05),("Ana",1.76)]#tabla de personas con alturas
def altura(persoa):
    return persoa[1]#ordena por altura de menor a mayor

tabla_alturas.sort(key=altura)
print(tabla_alturas)

#Funciones y diccionarios

def saudar (lingua):
    def saudar_es():
        print("Hola")
    def saudar_gl():
        print("Ola")
    def saudar_en():
        print("Hello")
    def saludar_ru():
        print("привет")
    def saludar_ma():
        print("هيلو")
    def saludar_be():
        print("ফলের")
    #diccionario
    func_saudo={"es":saudar_es,#solo hacemos referencia
                "gl":saudar_gl,
                "en":saudar_en,
                "ru":saludar_ru,
                "ma":saludar_ma,
                "be":saludar_be}

    return func_saudo[lingua] #devuelve del diccionario el codigo elegido
f=saudar("ru")#guara la referencia pero no el contenido
print(f)#muestra referencia
f()#desglosa el contenido
saudar("ma")()
saudar("be")()

l6=[1,2,3,4]

def es_par(n):
    return n%2==0
l2= filter(es_par,l6)#compara numeros de l6 con funcion es_par para sacar pares

l2= filter(lambda n: n % 2 == 0, l6)

for n in l2:
    print(n)
#Filtrar y trabajar con listas
#Filter,map,reduce

l3=[n+1 for n in l6]#sumamos uno a cada elemento de l

print(l3)

l4=[n for n in l6 if n%2==0]
print(l4)
m=["=","*"]
z=[]
for s in m:
    for n in l6:
        if n<4:
            z.append(n*s)#añade elementos n veces como elemento menor que cuatro

print(z)

z2=[n*s for s in m
    for n in l6
    if n<4]#forma parecida de hacerlo pero mas compacta
print(z2)


x2=(n**2 for n in l6)#objeto generador de datos

for n in x2:
    print(n)#saca datos elevados a 2

def mi_range(fin,inicio=0,salto=1):
    while inicio<=fin :
        yield inicio #retorna valor pero continua ejecutandose sin salir del bucle
        inicio = inicio + salto

x3=mi_range(inicio=4,fin=99,salto=15) #generador de rango

l7=[n for n in x3]

for n in x3 :
    print(n)#ejecucion de una sola vez
print(l7)

#Decoradores
#Añadir funcionalidad sin tocar la original

def mi_decorador(funcion_origen):
    def funcion_envolvente():
        print("Intrucciones antes de funcion original")
        funcion_origen()
        print("Instrucciones para despues de funcion origen")
    return funcion_envolvente

@ mi_decorador #otra forma de hacerlo
def funcion_necesita_decoracion():
    print("precio decoracion")


#funcion_necesita_decoracion= mi_decorador(funcion_necesita_decoracion)#Se emplea para realizar pruebas previas y posteriores
funcion_necesita_decoracion()

autenticado = False #True para permitirle saludar

def requiere_autentificacion(f):
    def funcion_decorada(*args, **kwargs):
        if autenticado:
            return f(*args, **kwargs)
        else:
            print ("Error el usuario no esta autenticado")
    return funcion_decorada

@requiere_autentificacion #recoge como paramentro la funcion de sauda
def sauda():
    print ("Hola")


sauda()
#requiere_autentificacion(sauda)() otro metodo para hacerlo


def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as fichero_abierto:
                saida=func(*args, **kwargs)
                fichero_abierto.write (f"{saida}\n")#crea linea por resultado de escritura y salida del fichero
        return decorador_funcion
    return decorador_log

@log('fichero,log')#recoge datos
def suma(a,b):
    return a+b

@log('fichero,log')#recoge datos
def resta(a,b):
    return a-b

@log('fichero,log')#recoge datos
def mult(a,b):
    return a*b

suma(1,1)
resta(7,25)
mult(8,1)





