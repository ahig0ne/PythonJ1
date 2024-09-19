#Solicite al usuario ingresar serie de numeros positivos y calcule e imprima el promedio de los numeros ingresados
def numerosPositivos():
    total = 0
    count = 0
    print('Ingrese serie de números positivos (ingrese un número negativo para finalizar)')
    
    while True:
        numeroIngresado = int(input('Ingrese número positivo: '))
        if numeroIngresado < 0:
            break
        total += numeroIngresado
        count += 1
    
    if count > 0:
        return f'El promedio de los números enteros positivos ingresados es: {total / count}'
    else:
        return 'No se ingresaron números positivos.'

if __name__ == '__main__':
    print(numerosPositivos())
