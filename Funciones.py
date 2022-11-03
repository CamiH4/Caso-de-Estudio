import Estructuras

def verificar_cuenta(lista_usuarios):
    try:
        numero_tarjeta = input("Digite el numero de su tarjeta: ")
        pin = input("Digite su pin: ")

        if(numero_tarjeta != lista_usuarios[0].Numero_de_tarjeta):
            return False
        if(pin != lista_usuarios[0].Pin):
            return False
        
        return True
    except Exception as ex:
        print(str(ex))
        
def depositar(saldo):
    try:
        deposito = int(input(
            "Ingrese la catidad a de efectivo a depositar C$: "))
        nuevo_saldo_deposito=0
        if(deposito % 100 == 0):
            nuevo_saldo_deposito = saldo + deposito
            return nuevo_saldo_deposito
        else:
            print("No puede realizar esta transacción")
    except Exception as ex:
        print(str(ex))

def retirar(saldo):
    try:
        nuevo_saldo_retiro=0
        retiro = int(input(
            "Ingrese la cantidad de efectivo a retirar C$: "))
        nuevo_saldo_retiro = saldo - retiro
        if(retiro %100 == 0):
            if(saldo >= 100):
                return nuevo_saldo_retiro
            else:
                print("Saldo insuficiente")
    except Exception as ex:
        print(str(ex))

def mostrar_saldo(saldo):
    print(saldo)
        