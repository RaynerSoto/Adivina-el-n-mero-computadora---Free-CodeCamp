import random


def computadora_adivina(x):
    contador = 0
    verdad = False
    limite_menor = -9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    limite_mayor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    while verdad == False:
        adivinanza = random.randrange(limite_menor,limite_mayor)
        if adivinanza == x:
            verdad = True
            print('La computadora a adivinado al número')
        else:
            if adivinanza > x and adivinanza < limite_mayor:
                limite_mayor = adivinanza
            else:
                limite_menor = adivinanza
            contador += 1
        print(adivinanza)
        print(f'Iteración: {contador}')

def juego():
    x = input('Ingrese el número entre -9999999999999999999999999999999999999999999999999999999999999999999999999999999'
              '999999999999999999999 y 999999999999999999999999999999999999999999999999999999999999999999999999999999999'
              '99999999999999999999\n')
    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        computadora_adivina(int(x))
    else:
        print('Esto no es número o por lo menos no por completo')
        print('Reintente')
        juego()