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



class ErroIdade(Exception):
    def __init__(self, edade):
        self.edade=edade
    def __str__(self):
        return "Error edad inadecuada :"+str(self.edade) + "incorrecta"



class Persona4:
    """Clase para definir unha persoa"""
    def __init__(self, nome,dni,edade,**outros):
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobarIdade(edade)


    def comprobarIdade(self,edade):
        if edade >=0 and edade < 100:
            return edade
        else:
            return ErroIdade(edade)
try:
    pepe = Persona4("Pepe","456k",30)

    juan = Persona4("Juan","456h",-60)
except ErroIdade as e:
    print("Error en creacion de persoa : "+str(e))