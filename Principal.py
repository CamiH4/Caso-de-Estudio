from Funciones import *
import Estructuras as struct
import os

lista_usuarios = []

usuario = struct.Cuenta_bancaria("Juan Isaac Osorio Rodriguez", "1147-5895-8896-6244", "4455", 5000)

lista_usuarios.append(usuario)

def menu():
    os.system('cls')
    print(f"""
1. Depositar
2. Retirar
3. Ver estado de cuenta
    """)
    opcion = int(input("Digite una opcion: "))
    return opcion

def mostar_menu():
    global lista_usuarios
    opcion=0
    os.system("cls")
    try:
        if(verificar_cuenta(lista_usuarios) == True):
            while(opcion != 3):
                opcion = menu()
                if opcion == 1: 
                    lista_usuarios[0].Saldo = depositar(lista_usuarios[0].Saldo)
                elif opcion == 2: 
                    lista_usuarios[0].Saldo = retirar(lista_usuarios[0].Saldo)
                elif opcion == 3: 
                    lista_usuarios[0] = mostrar_saldo(lista_usuarios[0].Saldo)
                else:
                    print("Opción inválida")
        else:
            print("Usuario no válido")
    except Exception as ex:
        print(str(ex))

def main():
    print("Bienvenido")
    os.system("pause")
    mostar_menu()

main()

