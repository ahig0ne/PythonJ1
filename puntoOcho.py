#Escriba programa que solicite numero y lo multiplique del 1 al 10
def numeroMult():
    print('Programa para multiplicar un numero del 1 al 10')
    numero = int(input('Por favor ingrese numero para multiplicar: '))
    for i in range(1,11,1):
        numeroTotal = numero * i
        print(f'{numero} multiplicado por {i} = {numeroTotal}')
        if i == 10:
            return

if __name__=='__main__':
    numeroMult()
    print('fin del programa')