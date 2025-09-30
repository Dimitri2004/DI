#Escepciones
def division (a,b):
    return a/b
try:
    division(1,0)
except ZeroDivisionError:#recoge escepcion y saca mensaje de error
    print("Operacion abortada, no se puede dividir por cero")
