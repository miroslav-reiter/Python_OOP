# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:54:12 2022

@author: Administrator
"""

class Kniha:
    ISBN = str() # ""
    nazov = str()
    autor = str()
    pocet_stran = int() # 0
    zaner = list() # []
    
 
print(Kniha)
print(type(Kniha))

print(Kniha())
print(type(Kniha()))

# class Auto:
#     znacka = str()
#     model = ()
#     VIN = ()
#     palivo = list()
    
#     def vypis_info(self):
#         print("VIN -->", self.VIN)
#         print("znacka -->", self.znacka)
#         print("model -->", self.model)
        
# Embecka = Auto()
# Embecka.nazov = "Skoda"
# Embecka.model = "Oktavia"
# Embecka.VIN = 6466326574
# Embecka.vypis_info()