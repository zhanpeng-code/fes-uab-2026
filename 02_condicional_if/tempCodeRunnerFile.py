any_de_traspàs = int(input("Introdueix un any: "))
if ((any_de_traspàs % 400) == 0 or (any_de_traspàs % 4)) == 0 and not((any_de_traspàs % 100) == 0):
    print(f"L'any {any_de_traspàs} és l'any de traspàs")
else:
    print(f"L'any {any_de_traspàs} no és l'any de traspàs")