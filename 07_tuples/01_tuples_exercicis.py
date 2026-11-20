# 📝 Exercicis sobre tuples


print("\nExercici 1:")
# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("Barcelona", "Mataró", "Sabadell", "Shanghai", "Girona")
print(ciutats[1], ciutats[-1])

print("\nExercici 2:")
# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
numeros = (1, 3, 5, 3, 7, 3, 9)
print(f"Hi ha {numeros.count(3)} treses.")

print("\nExercici 3:")
# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar(numeros):
    numeros = list(numeros)
    numeros.sort()
    return tuple(numeros)
numeros = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
print(ordenar(numeros))