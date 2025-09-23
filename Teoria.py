class Persona:
    """Clase para definir unha persoa"""
    def __init__(self, nome,dni,edade):
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobar_edad(edade)


    def comprobar_edad(self,edad):
        if 0 <= edad < 100:
            return edad
        else:
            return 0



p = Persona("Manuel", "354L",35)
p.edade = -1
print(p.edade)
print(p.nome)


class Posto:
    def __init__(self,tarea,horario,remuneracion,formacion):
        self.tarea = tarea
        self.horario = horario
        self.remuneracion = remuneracion
        self.formacion = formacion

class Traballador (Posto, Persona):
    def __init__(self, nome, dni, edad, tarea, horario, remuneracion,formacion,NUSS):
        super().__init__(nome,dni,edad)
        super().__init__(tarea,horario,remuneracion,formacion)
        self.NUSS = NUSS

class Persona2:
    """Clase para definir una persona"""
    def __init__(self,nome,dni,edade,**outros):
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobarEdade(edade)

    def comprobarEdade(self,edade):
        if (edade>=0) and edade <100:
            return edade
        else:
            return 0

class Posto2:
    def __init__(self,tarea,horario,salario,formacion,**outros):
        self.tarea = tarea
        self.horario = horario
        self.salario = salario
        self.formacion = formacion

class Trabajador2 (Persona2,Posto2):
    def __init__(self,nome,dni,edade,tarea,horario,salario,formacion,NUSS):
        super().__init__(nome=nome,dni=dni,edade=edade,tarea=tarea,horario=horario,salario=salario,formacion=formacion)
        self.NUSS = NUSS

t2 = Trabajador2("Juan",5679,45,"Soldador",7,2300,"CM","13515/UN")
print(t2.formacion)

