# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:29:09 2022

@author: Administrator
"""

# Dátové (typy) štruktúry
# 1. List (Zoznam) - indexovatelne, usporiadane poradie, menitelne, umoznuju duplicitne hodnoty
# 2. Tuple (Tica) - indexovatelne, usporiadane poradie, nemenitelne, umoznuju duplicitne hodnoty
# 3. Dictionary (Slovník) - indexovatelne-pomocou keys, usporiadane poradie, menitelne, neumoznuju duplicitne hodnoty
# 4. Set (Množina) - neidexovatelne, *neusporiadane poradie, **nemenitelne, neumoznuju duplicitne hodnoty

# * - od verzie python 3.7 su polozky usporiadane, na verzii 3.6 a menej neusporiadane ** - daju sa vsak pridat a odstranit hodnoty

# Zoznam - list - []
zoznam_cisel = ["0905123146","0908147893"]
zoznam_budov = list()

# Tica (Nemenny zoznam) - tuple ()
tica_firmy = ("IBM", "Dell", "SAP", "Google")
tica_velkost_tricka = tuple(("XL","S","M","L"))

# Dictionary (Slovník) - {kluc : hodnota} {key : value} {kluc je vlastny index}
# JSON
slovnik_kontakty = {"Mama":"0903156397", "Sef":"0915361784"}
slovnik_smajliky = dict({":-)":"usmievajuci", ":-(": "mraciaci sa"})
rodina = {"mama":"maria", "otec":"karol","brat":"dusan", "brat2":"dusanko"}

print(rodina["mama"])
print(tica_firmy[0])
print(zoznam_cisel[0])

# Standardne funkcie, len, max, min, sorted
print("Pocet prvkov/clenov rodiny --> ", len(rodina))
print("Zoradeny slovnik A-Z --> ", sorted(rodina))
print("Zoradena tica A-Z --> ", sorted(tica_firmy))

print("Zoradeny slovnik Z-A --> ", sorted(rodina, reverse=True))
print("Zoradena tica Z-A --> ", sorted(tica_firmy, reverse=True))

# Mnozina Set - {} hodnoty
mnozina_farieb = {"modra", "cervena", "hneda", "oranzova", "modra"}
