'''2.3,2.4,3.1'''
from tty import IFLAG


#Ejercicio 2.3

def gradosCelsius(grado):
    f=(grado-32)*5/9
    return f

#Ejercicio 2.4
def grad():
    for x in range(10,120,10):
        p=(gradosCelsius(x))
        print(p, "ªC")

#Ejercicio 3.1
def calculoSegundos(horas):
    g:int=horas*60*60
    y:int=g*60
    t:int=horas
    d=t//24

    while g > 59:
        g = g-60
        y +=1
    while y > 59:
        y -=60
        t +=1
    while t>23:
        t=t-24

    print(g,"seg",y,"min",t,"h",d," dias")

def calculoHoras(segundos):
    #segundos

    h: int= segundos//3600
    s : int= segundos//60
    m: int = segundos //60
    while s>60:
        s=s-60
        m=m+1
        while  m>60:

            m=m-60
            h = h+1
            while h>24:
                h=h-24
                h=h+1
    print(h,m,s)

#calculoHoras(60000000)
calculoSegundos(72)
#grad()