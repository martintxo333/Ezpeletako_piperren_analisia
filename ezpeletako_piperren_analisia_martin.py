# ==============================================================================
#  EZPELETAKO PIPERREN 2024KO PRODUKZIOAREN ANALISIA PANDAS BIDEZ
# ===============================================================================

# Ezpeletako piperraren 2024ko ekoizpena aztertzeko programa.
# Frantziako gobernuaren dataset ofiziala kargatzeko eta esploratzeko pandas erabiltzen da,
#estatistikak ateraz eta udalerriaren arabera datuak multzokatuz.
# Izenak euskerara itzultzen dira eskuz eta
# Azkenik, matplotlib-ek grafiko bat sortzen du herri bakoitzean zenbat piperlandare dauden erakutsiz.
# CSV-a gobernu frantsesak daukan https://www.data.gouv.fr/ publikotik ateratakoak dira:
"https://www.data.gouv.fr/datasets/piment-despelette-aop-productions-2024/"

import pandas as pd #pandas liburutegia datuak edo tablak manipulatzeko erabiltzen den tresna nagusia
import matplotlib.pyplot as plt #matplotlib.pyplot grafikoak marrazteko
import numpy as np #Numpy operazio matematikoak egiteko, arry.ekin. Bazpare inportatu zen

# ----------------------------------------------------------
# 1. Dataseta kargatu eta ikertu
# ----------------------------------------------------------

# CSV-a inportatu (kasu honetan ; erabiltzen du separadore moduan)
taula = pd.read_csv("piment-despelette-aop-productions-2024.csv", sep=";") #CSV kargatu DataFrame batean "taula" deituko duguna.

print ("Ezpeletako piperraren 2024ko ekoizpenaren analisia.")
print ("Programak CSV ofiziala kargatzen du, oinarrizko estatistikak kalkulatzen ditu eta grafiko bat erakusten du, herri bakoitzean zenbat piperlandare dauden erakutsiz")

print("\n========== LEHENENGO FILAK KONPROBATZEKO ==========")
print(taula.head()) #lehenengo 5 filak erakusten ditu, konprobatzeko ondo irakurri dela

print("\n========== DATU MOTAK ==========")
print(taula.dtypes) #Zutabe bakoitzaren datu mota erakusten du. Konprobatzeko ondo irakurri duen (zenbakiak zenbaki bezela eta ez object bezela, adibidez)

print("\n========== CSV-aren DIMENTSIOAK ==========")
print("Filas, Columnas:", taula.shape) #CSV-aren dimentsioak


# ----------------------------------------------------------
# 2. Estadistika basikoak
# ----------------------------------------------------------

print("\n========== ESTADISTIKA BASIKOAK ==========")
print(taula.describe())

# Count: zenbat erregistro dauden zutabe bakoitzeko
# mean: zutabe bakoitzeko media
# std: Desbiazio estandarra, zenbat aldatzen diren baloreak mediarekiko (geroz eta altuagoa, gehiago aldatzen dira datuak beraien artean)
# min: balio minimoa zutabe bakoitzean
# 25%: Lehenengo kuartila (balioen %25-a zenbaki hori baino txikiagoak dira)
# 50%: Mediana (datuak bi parte berdinetan banatu: partzelen erdiak 9.500 landare baino gehiago ditu eta beste erdiak gutxiago)
# 75%: Hirugarren kuartila (balioen %75-a zenbaki hori baino txikiagoak dira)
# maxi: balio maximoa zutabe bakoitzean


# --------------------------------------------------------------
# 3. Landare kopurua (Nbre de Pieds) lapurdiko herri bakoitzeko
# -------------------------------------------------------------
"""Database-an herri bakoitzeko baserri desberdin asko daude,
herri berdineko baserriak bateratzen dituen funtzioa:"""

# Filak taldekatu udalerriaren (Communes)-aren arabera
sum_by_commune = (
    taula.groupby("Communes")["Nbre de Pieds"]
    .sum() # Gehitu piperlandare kopurua (Nbre de Pieds)
    .sort_values(ascending=False) # Ordenatu zutabeak produkzio handienetik txikienera
)

print("\n========== PIPERRAREN EKOIZPENA HERRI BAKOITZEKO ==========")
print(sum_by_commune) #Serie berria inprimatzen du udalerri bakoitzeko produkzio totalarekin

# ----------------------------------------------------------
# 4. Zutabe bakoitzaren media (bakarrik numerikoak direnak, noski)
# ----------------------------------------------------------

mean_values = taula.mean(numeric_only=True) # Zutabe NUMERIKOEN media kalkulatu

print("\n========== ZUTABE BAKOITZAREN MEDIA ==========")
print(mean_values) # Batazbestekoak erakutsi

# -----------------------------------------------------------------
# 5. Grafikatu: herri bakoitzeko ekoizpena (izenak euskerara itzuli)
# -------------------------------------------------------------------

# --- Herriak euskerara pasa ---

euskal_izenak = {
    "ESPELETTE": "Ezpeleta",
    "USTARITZ": "Uztaritze",
    "CAMBO-LES-BAINS": "Kanbo",
    "LARRESSORE": "Larresoro",
    "lARRESSORE": "Larresoro",   # bi aldiz dago CSV-an gaixki idatzi zutelako
    "ST PEE/NIVELLE": "Senpere",
    "SOURAIDE": "Zuraide",
    "ITXASSOU": "Itsasu",
    "AINHOA": "Ainhoa",
    "HALSOU": "Haltsu",
    "JATXOU": "Jatsu"
}

# --- Indizea euskal izenekin jarri ---
sum_by_commune_eus = sum_by_commune.rename(index=euskal_izenak)

# --- Grafikoa sortu ---
plt.figure(figsize=(12, 7)) # 12x7 pulgada
plt.bar(sum_by_commune_eus.index, sum_by_commune_eus.values)

plt.xticks(rotation=80)
plt.ylabel("Landare kopurua (Pieds kopurua)")
plt.title("Piper ekoizpen totala herri bakoitzeko (AOP Ezpeleta 2024)")
plt.grid(True) #kuadrikula bat jarri azpitik
plt.tight_layout()

# --- Grafikoa erakutsi ---
plt.show()
