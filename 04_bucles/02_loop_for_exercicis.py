###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
print("\nExercici 1:")
parell = [num for num in range(2,21) if num % 2 == 0]
print (list(parell))

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
print("\nExercici 2:")
numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
suma = 0
for num in numeros:
    suma += num
mitjana = suma / len(numeros)
print(mitjana)

print("\nExercici 3:")
# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
max = numeros[0]
for num in numeros:
    if max < num:
        max = num
print(f"El número màxim de la llista és: {max}")

print("\nExercici 4:")
# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
list_comprehension = [paraula for paraula in paraules if len(paraula) > 5]
print(list_comprehension) 

print("\nExercici 5:")
# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
lletra = input("Introdueix una lletra: ").lower()
comptador = 0
for paraula in paraules:
  if paraula.startswith(lletra):  # Comparem en minúscules
    comptador += 1
print(f"Hi ha {comptador} paraules que comencen per la lletra {lletra}")

print("\nExercici 6:")
# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
mitjana = 0
for tension in tensions:
   mitjana += tension
print (f"La mitjana dels tensions registrats és {mitjana/len(tensions)}")

print("\nExercici 7:")
# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
corrent = [12/resistencia for resistencia in resistencies]
print(corrent)

print("\nExercici 8:")
# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
comptador = 0
for nivell in nivells_soroll:
   if nivell > -80:
      comptador += 0
print(f"Hi ha {comptador} nivells de soroll que ha superat el llindar de -80dBm")

print("\nExercici 9:")
# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
error = 0
i = 0
for bit in bits_transmesos:
   if bit != bits_rebuts[i]:
      error += 1
   i += 1
print(f"La taxa d'error és {error / len(bits_rebuts)}")

print("\nExercici 10:")
# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.
periodes = [1/frequencia for frequencia in frequencies]
print(periodes)