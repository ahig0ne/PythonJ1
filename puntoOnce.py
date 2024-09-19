def valorEnergia():
    # Solicitar datos
    MesConsumo = input('Ingrese el mes de consumo: ')
    valorKw = float(input('Ingrese el valor del kW (en moneda local): '))
    valorConsumido = float(input('Ingrese el total de kW consumidos en el mes: '))
    estrato = int(input('Ingrese el estrato (1-6): '))

    # Calcular el valor a pagar
    valorTotal = valorConsumido * valorKw

    # Aplicar descuentos según el estrato
    if estrato == 1:
        descuento = 0.50
        valorTotal *= (1 - descuento)
    elif estrato == 2:
        descuento = 0.30
        valorTotal *= (1 - descuento)
    elif estrato == 3:
        descuento = 0.15
        valorTotal *= (1 - descuento)
    
    # Estrato 4, 5 y 6 no tienen descuento ni recargo

    # Mostrar el resumen
    print(f'\nResumen de la factura de energía eléctrica:')
    print(f'Mes de consumo: {MesConsumo}')
    print(f'Total de kW consumidos: {valorConsumido} kW')
    print(f'Valor a pagar: {valorTotal:.2f} (en moneda local)')

if __name__ == '__main__':
    valorEnergia()

