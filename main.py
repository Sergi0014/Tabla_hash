from os import system
import random
from nodo import Nodo
from lista_hash import ListaHash
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

TablaHash = []
for i in range(5):
    TablaHash.append(ListaHash())
   
#crear un elemento para ejecutar el elemento hash
h = ListaHash()

while True:
    print("1. Registrar empleado")
    print("2. Mostrar empleados")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        clear()
        nombre = input("Ingrese el nombre del empleado: ")
        codigo = sum([ord(c) for c in nombre]) + len(TablaHash[0].recorrer()) + random.randint(1, 100)
        clave = h.funcion_hash(codigo) % len(TablaHash)
        TablaHash[clave].insertar(codigo, nombre)
        print(f"El usuario {nombre} ha sido ingresado correctamente.")
        
        
    elif opcion == "2":
        clear()
        for i in range(5):
            print("ListaHash["+ str(i) + "] = ",end="") 
            print(TablaHash[i].recorrer())
            print("\n")
                
    
    elif opcion == "3":
        clear()
        nombre = input("Ingrese el nombre del empleado a buscar: ")
        for lista in TablaHash:
            empleado = lista.buscar_por_nombre(nombre)
            if empleado:
                print(f"El empleado {empleado.nombre} con valor {empleado.codigo} ha sido encontrado.")
                break
        else:
            print(f"El empleado {nombre} no existe.")
        
    elif opcion == "4":
        clear()
        nombre = input("Ingrese el nombre del empleado a eliminar: ")
        for lista in TablaHash:
            if lista.eliminar_por_nombre(nombre):
                print(f"El empleado {nombre} ha sido eliminado correctamente.")
                break
        else:
            print(f"El empleado {nombre} no existe.")
        
    elif opcion == "5":
        break
print ("\nEl programa ah finalizado\n")
    