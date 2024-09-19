#Programa que solicita al usuario su edad y luego determine si es mayor de edad o no utilizando una declaracion if.
def mayorMenor():
    edad = int(input('Ingrese su edad: '))
    #condiciones para enviar cierto mensaje al ser menor o mayor de edad.
    if (edad>=18):
        return('Eres mayor de edad')
    else:
        return('Eres menor de edad')
if(__name__=='__main__'):
    print(mayorMenor())