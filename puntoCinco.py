def paisContinente():
    pais = str(input('Ingrese pais\ncolombia -- EstadosUnidos\nAustralia -- Japon\nInglaterra -- Nigera\nPais: ')).lower()
    match pais:#Si el pais coincide con el continente 
        case 'colombia':
            continentePais = 'sur america'
        case 'estadosunidos':
            continentePais = 'america'
        case 'australia':
            continentePais = 'oceania'
        case 'japon':
            continentePais = 'asia'
        case 'inglaterra':
            continentePais = 'europa'
        case 'nigeria':
            continentePais = 'africa'
        case _:
            return('pais no listado')

    return(f'{continentePais} es el continente de {pais}')
if __name__=='__main__':
    print(paisContinente())