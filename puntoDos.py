#Solicite al usuario ingresar calificación
def calificacion():
    calificacionEstudiante= int(input('Por favor seleccione su calificacion del 0 al 100: '))
    #condicionales para declarar si el estudiante aprobó o no
    if(calificacionEstudiante>=60):
        return('felicidades, ha aprobado.')
    else:
        return('usted no ha aprobado.')
#proteccion principal
if (__name__=='__main__'):
    print(calificacion())