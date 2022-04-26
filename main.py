from datetime import datetime


nombreEmpleados = []
apellidoEmpleados = []
sueldoBaseEmpleados = []
fechaIngresoEmpleados = []
cantidadHijosEmpleados = []
tipoEmpresaEmpleados = []
baseImponibleEmpleados=[]

def verifNP(nombre, apellido):
    while not nombre.isalpha():
        print("nombre no valido, no se aceptan caracteres numericos ni simbolos.")
        nombre=input("vuelva a introducir el nombre, por favor:")
    else:
        nombreEmpleados.append(nombre)

    while not apellido.isalpha():
        print("apellido no valido, no se aceptan caracteres numericos ni simbolos.")
        apellido = input("vuelva a introducir el apellido, por favor:")
    else:
        apellidoEmpleados.append(apellido)

def verifSueldo(sueldoBase):
    while not sueldoBase.isnumeric():
        print("sueldo base no valido, no se aceptan letras ni simbolos especiales.")
        sueldoBase=input("introduzca de nuevo su sueldo base por favor")
    else:
        sueldoBaseEmpleados.append(sueldoBase)

def convFecha(fechaIngreso):
    global fecha_dt
    fecha_dt = datetime.strptime(fechaIngreso, '%d/%m/%Y')
    fechaIngresoEmpleados.append(fecha_dt)

def verifTipoEmpresa(tipoEmpresa):
    while tipoEmpresa != 1 and tipoEmpresa != 2:
        print('tipo de empresa invalida, ingrese nuevamente tipo de empresa')
        tipoEmpresa = int(input('ingrese 1 o 2 dependiendo del tipo de empresa al que pertenece: '))
        tipoEmpresaEmpleados.append(tipoEmpresa)


def cobroXEmpresa(tipoEmpresaEmpleados,sueldoBaseEmpleados): # Los empleados están en una de dos empresas de sso: la primera cobra (entre imposición y otros gastos) el 12 % de la base imponible, mientras que la segunda cobra el 11.4%
for empresa in tipoEmpresaEmpleados:
        if empresa==1:
         for sueldoBase in sueldoBaseEmpleados:
          cobroE1=((12 * sueldoBase) / 100)
          print(f'el cobro por el tipo de empresa 1 es de:', cobroE1)
        else:
        # for sueldoBase in sueldoBaseEmpleados:
cobroE2=((11.4 * sueldoBase) / 100)
            print(f'el cobro por el tipo de empresa 2 es de:', cobroE2)



def pedirDatos():
    global nombre
    global apellido

    nombre = input('ingrese su nombre: ')
    apellido = input('ingrese su apellido: ')
    verifNP(nombre,apellido)


    global sueldoBase
    sueldoBase = int(input('ingrese su sueldo base: '))
    verifSueldo(sueldoBase)


    global fechaIngreso
    fechaIngreso = input('ingrese fecha de ingreso en formato DD/MM/AA: ')
    convFecha(fechaIngreso)

    global cantidadHijos
    cantidadHijos = int(input('ingrese cantidad de hijos'))
    if cantidadHijos <0:
        cantidadHijos = int(input('ingrese cantidad de hijos correcta: '))
    cantidadHijosEmpleados.append(cantidadHijos)

    tipoEmpresa = int(input('ingrese 1 o 2 dependiendo del tipo de empresa al que pertenece: '))
    verifTipoEmpresa(tipoEmpresa)
    tipoEmpresaEmpleados.append(tipoEmpresa)


    print(nombreEmpleados)
    print(apellidoEmpleados)
    print(sueldoBaseEmpleados)
    print(fechaIngresoEmpleados)
    print(cantidadHijosEmpleados)
    print(tipoEmpresaEmpleados)

for i in range(10):
    i = 0
pedirDatos()
    i += 1

def difM(fecha_dt, fechaActual):
    for fecha_dt in fechaIngresoEmpleados:
        global mesT
        mesT=(fechaActual.year - fecha_dt.year) * 12 + fechaActual.month - fecha_dt.month
        print(f'estos son los meses trabajados:',mesT)
        global mesesTrabajados
        mesesTrabajados=[]
        mesesTrabajados.append(mesT)


difM(fecha_dt, fechaActual=datetime.now())


# def bonificacion(sueldoBase):  # Una bonificación del 1% del sueldo base, por cada mes trabajado
def bonMes(sueldoBaseEmpleados):
    for sueldoBase in sueldoBaseEmpleados:
        for mes in mesesTrabajados:
         global bonXM
         bonXM = (sueldoBase * (1 / 100)) * mesT
         print(f'la bonificacion por mes trabajado es de: ', bonXM)

bonMes(sueldoBaseEmpleados)



def promedioPagos(sueldoBaseEmpleados):
    promedioPagos = (sum(sueldoBaseEmpleados) / len(sueldoBaseEmpleados))
    print(f'el promedio del sueldo base de los 10 empleados es de :', promedioPagos)


promedioPagos(sueldoBaseEmpleados)

def baseImponible(sueldoBase, sueldoBaseEmpleados):# base imponible con hijos.La suma de los tres valores anteriores, conforman la “base imponible”.
global BI
    BI = bonXM + sueldoBase + aFam  # base imponible si tiene hijos
for sueldoBase in sueldoBaseEmpleados:
       print(f'su base imponible, para empleado con hijos es de:', BI)
       baseImponibleEmpleados.append(BI)

def baseImponibleSH(sueldoBase, sueldoBaseEmpleados, aFam=0): #base imponible sin hijos
BI = bonXM + sueldoBase + aFam   # base imponible si no tienes hijos
for sueldoBase in sueldoBaseEmpleados:
      print(f'su base imponible, para empleado sin hijos es de:', BI)
      baseImponibleEmpleados.append(BI)


def asignFam(cantidadHijos):  # Una asignación familiar del 5% del sueldo base, por cada hijo
for numeroHijos in cantidadHijosEmpleados:
        global aFam
        aFam = ((5 * sueldoBase) / 100) * numeroHijos
        if numeroHijos != 0:   # si tiene hijos
print(f'la cantidad de hijos que tiene es: {numeroHijos} y su asignacion familiar es: {aFam}')
            baseImponible(sueldoBase, sueldoBaseEmpleados)
        else:
            print(f'no tiene hijos y su asignacion familiar es equivalente a su sueldo base: {sueldoBase} ')
            baseImponibleSH(sueldoBase, sueldoBaseEmpleados, aFam)


asignFam(cantidadHijos)

def cotizSalud(baseImponibleEmpleados):# Todos los empleados deben cotizar el 7% de la base imponible en salud.
for BI in baseImponibleEmpleados:
        cotizSalud = ((7 * BI) / 100)
        print(f'su cotizacion en salud es:', cotizSalud)

cotizSalud(baseImponibleEmpleados)
cobroXEmpresa(tipoEmpresaEmpleados, sueldoBaseEmpleados)
