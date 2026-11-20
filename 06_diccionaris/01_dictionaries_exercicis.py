###
# EXERCICIS (diccionaris)
###
print("\nExercici 1:")
# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.
estudiant = {
    "nom": "Zhanpeng",
    "edat": 19,
    "assignatures": ["FES", "CiCE", "RiOG"]
}
for clau, valor in estudiant.items():
    print (f"{clau}: {valor}")

print("\nExercici 2:")
# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.

print(estudiant["assignatures"][1])
estudiant["edat"] = 16
print(estudiant["edat"])

print("\nExercici 3:")
# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.
estudiant["grau"] = "Enginyeria de Sistemes de Telecomunicació"
del estudiant["edat"]
for clau, valor in estudiant.items():
    print (f"{clau}: {valor}")

print("\nExercici 4:")
# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.
print(f"Existència de nom: {"nom" in estudiant}")
print(f"Existència de email: {"email" in estudiant}")

print("\nExercici 5:")
# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".
for clau, valor in estudiant.items():
    print (f"{clau}: {valor}")

print("\nExercici 6:")
# Exercici 6: Comptar paraules
# Donada la llista de paraules:
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.
recompte = {}
for paraula in paraules:
  if paraula in recompte:
    recompte[paraula] += 1
  else:
    recompte[paraula] = 1
print(recompte)