#solicite ingresar tres longitudes y determinar si pueden formar un triangulo valido.
def LongitudTotal():
    print('Por favor ingrese tres longitudes para determinar si es un triangulo valido: ')
    longitudUno=int(input('Longitud uno: '))
    longitudDos=int(input('Longitud dos: '))
    longitudTres=int(input('Longitud tres: '))

    if longitudTres + longitudUno > longitudDos and longitudUno + longitudDos > longitudTres and longitudDos + longitudTres > longitudUno:
        return('triangulo valido')
    else:
        return('triangulo no valido')
if __name__=='__main__':
    print(LongitudTotal())