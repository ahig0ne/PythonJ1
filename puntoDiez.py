def informacionEmpleado():
    # Solicitar información del empleado
    nombre = input('Ingrese el nombre del empleado: ')
    apellidos = input('Ingrese los apellidos del empleado: ')
    telefono = input('Ingrese el teléfono del empleado: ')
    ingreso = int(input('Ingrese el año de ingreso a la empresa: '))
    edad = int(input('Ingrese la edad del empleado: '))

    # Calcular la antigüedad
    actual = 2024
    antiguedad = actual - ingreso

    # Imprimir la información del empleado
    print('Información del Empleado:')
    print(f'Nombre: {nombre}')
    print(f'Apellidos: {apellidos}')
    print(f'Antigüedad en la empresa: {antiguedad} años')

if __name__ == '__main__':
    informacionEmpleado()
