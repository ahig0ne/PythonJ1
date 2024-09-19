#solicite al user ingresar dia, mes y year
def fechaCompleta():
    print('Escriba una fecha: ')
    dia=int(input('Ingrese dia: '))
    mes=int(input('Ingrese mes: '))
    bisiesto=int(input('Si el año es bisiesto, ponga 1, de lo contrario, 0: '))
    year=int(input('Ingrese año: '))
    if dia <=30 and mes<=12 and year>=0:
        if bisiesto == 0 and mes==2 and dia<=28:
            return(f'{dia}/{mes}/{year} es una fecha valida')
        elif bisiesto == 0 and mes==2 and dia>28:
                print(f'{dia}/{mes}/{year} es una fecha invalida')
        if bisiesto == 1 and mes==2 and dia<=29:
            return(f'{dia}/{mes}/{year} es una fecha valida')
        elif bisiesto == 1 and mes == 2 and dia>=30:
            return(f'{dia}/{mes}/{year} es una fecha invalida')
        return (f'{dia}/{mes}/{year} es una fecha valida')
    
    else:
        return('fecha incorrecta')
    
if __name__=='__main__':
    print(fechaCompleta())