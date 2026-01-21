import os

ARCHIVO_CLUBES = "clubes.txt"
ARCHIVO_MIEMBROS = "miembros.txt"

lista_clubes = []
lista_miembros = []


def cargar_archivos():
    global lista_clubes, lista_miembros

    if os.path.exists(ARCHIVO_CLUBES):
        with open(ARCHIVO_CLUBES, 'r', encoding='utf-8') as f:
            lista_clubes = [linea.strip() for linea in f if linea.strip()]

    if os.path.exists(ARCHIVO_MIEMBROS):
        with open(ARCHIVO_MIEMBROS, 'r', encoding='utf-8') as f:
            for linea in f:
                if linea.strip():
                    datos = linea.strip().split('|')
                    if len(datos) == 3:
                        lista_miembros.append({
                            'numero': datos[0],
                            'nombre': datos[1],
                            'club': datos[2]
                        })


def registrar_club():
    print("\n Registrar club ")
    nombre_club = input("Nombre del club: ").strip()

    if nombre_club and nombre_club not in lista_clubes:
        lista_clubes.append(nombre_club)
        with open(ARCHIVO_CLUBES, 'a', encoding='utf-8') as f:
            f.write(nombre_club + '\n')
        print("Club registrado correctamente")
    elif nombre_club in lista_clubes:
        print("El club ya existe")
    else:
        print("Nombre no válido")


def registrar_miembro():
    print("\n Registrar miembro ")

    if not lista_clubes:
        print("No hay clubes. Registra uno primero")
        return

    numero = input("Número: ").strip()
    nombre = input("Nombre: ").strip()

    print("\nClubes disponibles:")
    for i, club in enumerate(lista_clubes, 1):
        print(f"{i}. {club}")

    try:
        seleccion = int(input("Selecciona club (número): "))
        if 1 <= seleccion <= len(lista_clubes):
            club_elegido = lista_clubes[seleccion - 1]
            registro = f"{numero}|{nombre}|{club_elegido}"

            lista_miembros.append({
                'numero': numero,
                'nombre': nombre,
                'club': club_elegido
            })

            with open(ARCHIVO_MIEMBROS, 'a', encoding='utf-8') as f:
                f.write(registro + '\n')

            print("Miembro registrado")
        else:
            print("Selección inválida")
    except:
        print("Entrada incorrecta")


def mostrar_clubes():
    print("\n Lista de clubes ")
    if not lista_clubes:
        print("No hay clubes")
    else:
        for i, club in enumerate(lista_clubes, 1):
            print(f"{i}. {club}")


def mostrar_miembros():
    print("\n Lista de miembros ")
    if not lista_miembros:
        print("No hay miembros")
    else:
        for i, m in enumerate(lista_miembros, 1):
            print(f"{i}. Número: {m['numero']} - Nombre: {m['nombre']} - Club: {m['club']}")


def menu_principal():
    while True:
        print("\n---- Menú de Clubes y Miembros ----")
        print("1. Registrar Club")
        print("2. Registrar Miembro")
        print("3. Ver Clubes")
        print("4. Ver Miembros")
        print("5. Salir")
        print("---------------------------------")

        opcion = input("Elige opción (1-5): ").strip()

        if opcion == "1":
            registrar_club()
        elif opcion == "2":
            registrar_miembro()
        elif opcion == "3":
            mostrar_clubes()
        elif opcion == "4":
            mostrar_miembros()
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida")


cargar_archivos()
menu_principal()
