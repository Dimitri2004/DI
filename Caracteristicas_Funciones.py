#Funciones

def nome_funcion (parametros1,parametros2):
    #instrucciones de la funcion
    print(parametros1)
    print(parametros2)


nome_funcion(5,"Hola")

#range(__stop=3,__start="Hola")

nome_funcion(parametros2=6.9,parametros1="Que buen dia para ser sabado")#Cambiar orden de los parametros dentro de funcion
#Otro tipo de funciones


def repetir_mensaje(mensaxe, veces = 1,*maismensaxes):
    print("E mais :"+str(len(maismensaxes)))
    print(mensaxe * veces)
    for outroMensaxe in maismensaxes:
        print(outroMensaxe*veces)


repetir_mensaje("Hola",6,"javier","pelota","nuez",3.5)


def persoa(nome,dni,**maisDatos):
    print("El nombre es:"+nome)
    print("El dni es :"+dni)
    for dato in maisDatos.keys():
        print("La ",dato," é:",maisDatos[dato])

persoa("Dima","7754623M",edad=21,localidad="ponevedra",ocupacion=False)



