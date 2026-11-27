###
# EXERCICIS - CSV
# Utilitza csv, UTF-8, newline="" i una carpeta temporal per a les proves.
###

import csv
from pathlib import Path
from tempfile import TemporaryDirectory

CAMPS = ["sensor", "valor", "unitat"]

# Exercici 1 - Bàsic - Taula de tensions
# Implementa desar_tensions(ruta, tensions) amb csv.writer.
# Escriu la capçalera ["sensor", "volts"] i les files rebudes.
# Amb les dades següents, csv.reader ha de recuperar
# [["sensor", "volts"], ["V1", "3.3"], ["V2", "5.0"]].
# Una llista buida ha de produir només la capçalera.
tensions = [("V1", 3.3), ("V2", 5.0)]
def desar_tensions(ruta, tensions):
    with open(ruta, "w", encoding="utf-8", newline="") as fitxer:
        esc = csv.writer(fitxer)
        esc.writerow(["sensor", "volts"]) 
        esc.writerows(tensions) 

# Exercici 2 - Bàsic - Selecció per llindar
# Implementa sensors_en_alerta(ruta, llindar) amb csv.DictReader.
# El CSV d'entrada té la capçalera sensor,valor,unitat i valors finits vàlids.
# Retorna els noms amb valor >= llindar, conservant l'ordre del fitxer.
# Amb les lectures següents i llindar 25.0 s'espera ["T2", "T3"].
# Amb només capçalera s'espera []. El valor igual al llindar s'inclou.
lectures = [
    {"sensor": "T1", "valor": 20.0, "unitat": "°C"},
    {"sensor": "T2", "valor": 25.0, "unitat": "°C"},
    {"sensor": "T3", "valor": 26.0, "unitat": "°C"},
]
def sensors_en_alerta(ruta, llindar):
    sensors_valides = []
    with open(ruta, "r", encoding="utf-8", newline="") as fitxer:
        for fila in csv.DictReader(fitxer):
            if float(fila["valor"]) >= llindar:
                sensors_valides.append(fila["sensor"])
    return sensors_valides

# Exercici 3 - Intermedi - Anada i tornada
# Implementa desar_lectures(ruta, lectures) i recuperar_lectures(ruta).
# Fes servir DictWriter/DictReader i la capçalera sensor,valor,unitat.
# Les entrades són diccionaris vàlids i els valors recuperats han de ser float.
# La llista següent s'ha de recuperar igual, incloent-hi la coma del nom.
# Una llista buida s'ha de recuperar com [], amb capçalera al fitxer.
lectures_amb_coma = [
    {"sensor": "Sala, nord", "valor": 19.5, "unitat": "°C"},
]
def desar_lectures(ruta, lectures):
    with open(ruta, "w", encoding="utf-8") as fitxer:
        esc = csv.DictWriter(fitxer, fieldnames=CAMPS)
        esc.writeheader()
        esc.writerow(lectures)

def recuperar_lectures(ruta):
    lectures = []
    with open(ruta, "r", encoding="utf-8", newline="") as fitxer:
        lectures = list(csv.DictReader(fitxer))
    for lectura in lectures:
        lectura["valor"] = float(lectura["valor"])
    return lectures

# Exercici 4 - Repte opcional - Capçalera incorrecta
# Implementa llegir_amb_capcalera_validada(ruta).
# Exigeix exactament sensor,valor,unitat en aquest ordre.
# Si falta la capçalera o és diferent, genera ValueError.
# Amb capçalera correcta, retorna una llista de diccionaris amb valor float.
# Per simplificar, les files posteriors a la capçalera són completes i vàlides.
# Entrada "nom,valor\nT1,20\n" genera ValueError.
# Entrada "sensor,valor,unitat\n" retorna []. Fitxer buit genera ValueError.
capcalera_incorrecta = "nom,valor\nT1,20\n"
def llegir_amb_capcalera_validada(ruta):
    with open(ruta, "r", encoding="utf-8", newline="") as fitxer:
        lector = csv.DictReader(fitxer)
        if lector.fieldnames != CAMPS:
            raise ValueError("La capçalera és incorrecta")
        lector = list(lector)
    for lectura in lector:
        lectura["valor"] = float(lectura["valor"])
    return lector

def main():
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "lectures.csv"
        print("\nExercici 1:")
        desar_tensions(ruta, [("V1", 3.3), ("V2", 5.0)])
        with open(ruta, encoding="utf-8", newline="") as fitxer:
            print(list(csv.reader(fitxer)))



if __name__ == "__main__":
    main()