###
# EXERCICIS (excepcions)
# Tots els textos d'entrada es proporcionen per evitar entrada interactiva.
###
import math
from pathlib import Path
from tempfile import TemporaryDirectory

# Exercici 1 - Bàsic. Conversió segura de tensions
# Per a cada text de tensions, intenta convertir-lo amb float.
# Captura ValueError i mostra 'Tensió incorrecta' en aquest cas.
# Utilitza else per mostrar la conversió quan sigui correcta.
# Sortida esperada, una línia per entrada: 3.3 / Tensió incorrecta / 0.0.
# Cas límit: '0' és una mesura vàlida.
tensions = ["3.3", "avaria", "0"]
# TODO: escriu el bucle i el tractament de ValueError.
for text in tensions:
    try:
        tension = float(text)
    except ValueError:
        print("Tensió incorrecte")
    else:
        print(tension)

# Exercici 2 - Bàsic. Humitat amb contracte
# Defineix validar_humitat(text) que retorni un float finit dins [0, 100].
# Genera ValueError per a text no numèric, valors no finits o fora de rang.
# Utilitza math.isfinite després de convertir el text.
# Entrades: '0', '100', '45.5', '-1', '101', 'nan', 'inf', 'error'.
# Retorns esperats per a les tres primeres: 0.0, 100.0 i 45.5.
# La resta han de produir ValueError, gestionat en les demostracions.
entrades_humitat = ["0", "100", "45.5", "-1", "101", "nan", "inf", "error"]
# TODO: defineix la funció i mostra resultats o un missatge de rebuig.
# import math
def validar_humitat(text):
    humitat = float(text)
    if not math.isfinite(humitat):
        raise ValueError("La humitat ha de ser finita.")
    if humitat < 0 or humitat > 100:
        raise ValueError("La humitat ha de estar entre o i 100")
    return humitat

for text in entrades_humitat:
    try:
        print(validar_humitat(text))
    except ValueError as error:
        print(error)

# Exercici 3 - Intermedi. Fitxer absent i finalització
# Dins de TemporaryDirectory crea només una ruta a 'absent.txt' amb Path.
# Intenta obrir-la en mode lectura, amb encoding='utf-8'.
# Captura FileNotFoundError i mostra 'Fitxer absent'.
# Utilitza finally per mostrar 'Intent acabat' tant si hi ha error com si no.
# Sortida esperada: Fitxer absent / Intent acabat.
# Segona prova: crea un fitxer temporal que contingui 'T1=21.5' i repeteix.
# Sortida esperada: T1=21.5 / Intent acabat.
# Mantén tots els fitxers dins de la carpeta temporal.
# TODO: importa Path i TemporaryDirectory i prova els dos camins.
# from pathlib import Path
# from tempfile import TemporaryDirectory

with TemporaryDirectory() as carpeta:
    ruta = Path(carpeta) / "absents.txt"

    # ruta.write_text("T1=21.5", encoding="utf-8")

    try:
        with open(ruta, encoding="utf-8") as fitxer:
            contingut = fitxer.read()
    except FileNotFoundError:
        print("Fitxer absent")
    else:
        print(contingut)
    finally:
        print("Intent acabat")

# Exercici 4 - Repte opcional. Filtrar lectures de temperatura
# Defineix filtrar_temperatures(textos) que retorni (valides, rebutjades).
# valides és la llista de floats finits dins del rang simulat [-40, 85] °C.
# rebutjades és el nombre d'entrades que no es poden acceptar.
# Crea una funció validar_temperatura(text) i reutilitza-la al bucle.
# Entrada següent. Retorn esperat: ([-40.0, 21.5, 85.0], 3).
# Amb [] ha de retornar ([], 0). Amb ['nan', 'inf'] ha de retornar ([], 2).
textos = ["-40", "21.5", "85", "86", "avaria", "nan"]
# TODO: captura ValueError per cada lectura i continua amb les següents.
# import math

def validar_temperatura(text):
    temperatura = float (text)
    if not math.isfinite(temperatura):
        raise ValueError("La temperatura ha de ser finita.")
    if temperatura < -40 or 85 < temperatura:
        raise ValueError("Temperatura ha de ser en interval [-40, 85]")
    return temperatura
    
def filtrar_temperatures(textos):
    valides = []
    rebutjades = 0
    for temp in textos:
        try:
            temperatura = validar_temperatura(temp)
        except ValueError:
            rebutjades += 1
        else:
            valides.append(temperatura)
    return valides, rebutjades

print(filtrar_temperatures(textos))
print(filtrar_temperatures([]))
print(filtrar_temperatures(["nan", "inf"]))