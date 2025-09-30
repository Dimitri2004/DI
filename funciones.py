#Escepciones
def division (a,b):
    return a/b

n1=1
n2=3  #str(2) + " Texto"
try:
    division(n1,n2)
except ZeroDivisionError:#recoge escepcion y saca mensaje de error
    print("Operacion abortada, no se puede dividir por cero")
except TypeError:#error de tipo
    print("Tipos inadecuados")
finally:
    print("Puede que si o no, se realice la division")



resultado = 0
try:
    resultado = division(n1,n2)
except (ZeroDivisionError,TypeError) as e:#recoge doble error en un solo print
    print("Error al realizar division "+str(e))
else:
    print("El resultado de la operacion es: "+str(resultado))

