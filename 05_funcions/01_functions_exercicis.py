###
# EXERCICIS (funcions)
###
print("\nExercici 1:")
# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
  print(f"{salutacio} {nom}!")
saludar_a("Zhanpeng")

print("\nExercici 2:")
# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
  return numero % 2 == 0

print(es_parell(8))  
print(es_parell(7))

print("\nExercici 3:")
# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma / len(numeros)
print(mitjana([1, 4, 9, 16, 25])) 
  

print("\nExercici 4:")
# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma
print(sumar_tot(2, 5, 10))

print("\nExercici 5:")
# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
  for i in range(1, limit + 1):
    print(f"{numero} * {i} = {numero * i}")
print(taula_multiplicar(5))

print("\nExercici 6:")
# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
  for clau, valor in kwargs.items():
    print(f"{clau}: {valor}")
mostrar_perfil(nom = "Zhanpeng", edat = 19, grau = "Enginyeria de Sistemes de Telecomunicació")

print("\nExercici 7:")
# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
  resultat = 1
  comptador = n
  while comptador >= 1:
    resultat *= comptador
    comptador -= 1
  return resultat

def maxim(numeros):
  max = numeros[0]
  for numero in numeros:
    if numero > max:
      max = numero
  return max

print(f"El factorial de 7 és {factorial(7)}")
print(f"El màxim és {maxim([15, 5, 25, 10, 20])}")

print("\nExercici 8:")
# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
  vocals = ["a", "e", "i", "o", "u", "à", "è", "é", "í", "ò", "ó", "ú", "ï", "ü"]
  comptador = 0
  for lletra in text.lower():
    if lletra in vocals:
      comptador += 1
  return comptador
print(f"Hi ha {comptar_vocals('Fonaments')} vocals a 'Fonaments'")


print("\nExercici 9:")
# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
  min = numeros[0]
  max= numeros[0]
  for numero in numeros[1:]:
    if numero < min:
      min = numero
    if numero > max:
      max = numero
  return min, max
min, max = minim_i_maxim([0, 2, 7, 3, 5, 9])
print(f"El mínim és {min} i el màxim és {max}") 

print("\nExercici 10:")
# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text):
  lletres = list(caracter.lower() for caracter in text)
  return lletres == lletres[::-1]

print(es_palindrom("radar"))