import random
import csv
import statistics

paises = ["Estados Unidos", "Canadá", "Alemania", "Francia", "Japón", "Australia", "Noruega", "Italia", "España", "Reino Unido"]

# Esta funcion sirve para generar donaciones aleatorias.
def generar_donaciones():
    donaciones = {}
    for pais in paises:
        donaciones[pais] = random.randint(10000, 100000)
    return donaciones

# Esta funcion sirve para clasificar donaciones
def clasificar_donaciones(donaciones):
    print("-- CLASIFICACION DE DONACIONES: -- \n")
    for pais, monto in donaciones.items():
        if monto < 30000:
            print(f"{pais}: {monto} -> Donación menor a $30,000")
        elif 30000 <= monto <= 70000:
            print(f"{pais}: {monto} -> Donación entre $30,000 y $70,000")
        else:
            print(f"{pais}: {monto} -> Donación mayor a $70,000")

# Esta funcion sirve para visualizar estadisticas de donaciones
def visualizar_estadisticas(donaciones):
    montos = list(donaciones.values())
    print("-- ESTADISTICA DE DONACIONES: -- \n")
    print(f"Donación mas alta -> {max(montos)}")
    print(f"Donación mas baja -> {min(montos)}")
    print(f"Promedio delas donaciones: {statistics.mean(montos)}")
    print(f"Desviacion estándar de donaciones: {statistics.stdev(montos)}")

# Esta funcion sirve para generar reporte de donaciones
def generar_reporte(donaciones):
    impuesto = 0.05
    gastos_administrativos = 0.08
    with open('reporte.csv', 'w', newline='') as csvfile:
        fieldnames = ['Pais', 'Donacion', 'Impuestos', 'Gastos Administrativos', 'Donacion Neta']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for pais, monto in donaciones.items():
            impuestos = monto * impuesto
            gastos = monto * gastos_administrativos
            donacion_neta = monto - impuestos - gastos
            writer.writerow({'Pais': pais, 'Donacion': monto, 'Impuestos': impuestos, 'Gastos Administrativos': gastos, 'Donacion Neta': donacion_neta})
    print("Reporte de donaciones generado correctamente")

def main():
    while True:
        print("\nMenu")
        print("1 - Generar donaciones aleatorias")
        print("2 - Clasificar donaciones")
        print("3 - Visualizar estadisticas")
        print("4 - Reporte de donaciones")
        print("5 - Salir del programa")

        opcion = input("Selecciona una opcion: ")

        if opcion == '1':
            donaciones = generar_donaciones()
            print("Donaciones generadas aleatoriamente.")
        elif opcion == '2':
            clasificar_donaciones(donaciones)
        elif opcion == '3':
            visualizar_estadisticas(donaciones)
        elif opcion == '4':
            generar_reporte(donaciones)
        elif opcion == '5':
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("Opcion no valida. Porfavor selecciona una opcion valida")
            break

if __name__ == "__main__":
    main()
