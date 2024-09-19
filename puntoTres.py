#solicite al usuario un numero entero positivo
def enteroPositivo():
    numeroEntero=(int(input('Ingrese numero entero positivo para imprimir los numeros desde ese hasta 1: ')))
    while numeroEntero!= 0:
        if numeroEntero>=1:
            print(numeroEntero)
            numeroEntero-=1
            if numeroEntero == 0:
                print('limite de enteros positivos alcanzados')
if __name__=='__main__':
    enteroPositivo()
    print(enteroPositivo())