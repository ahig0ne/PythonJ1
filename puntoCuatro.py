#solicite al usuario contraseña y vericique si tiene 8 caracteres
def verificacionClave():
    numero ='0123456789'
    letras=0
    a=0
    constrasena = str(input('Por favor ingrese contraseña con mas de 8 palabras y al menos un numero: '))
    for i in constrasena:
        if i in numero:
              a+=1
    if ((a>=1) == (len(constrasena)>=8)):
         return('Contraseña valida')
    else:
         return('Contraseña invalida')
if (__name__=='__main__'):
     print(verificacionClave())