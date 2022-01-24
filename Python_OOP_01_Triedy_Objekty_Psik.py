# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:49:17 2022

@author: Administrator
@version: 1.0
"""
class Psik:
    """ Trieda manual/navod ako vytvarat objekty 
        Kuchar - recept podla, ktoreho navarim jedlo
        Architekt - plan podla, ktorreho postavam budovu
        Trieda (abstraktne) - blueprinty
        Objekt (konkretne) - instancie triedy
    
    """
    # pass
    # Vlastnosti/atributy/data/datove zlozky/premenne (variables)
    rasa = "" # str()
    jeLenivy = False # bool()
    meno = str()
    vek = 0 # int()
    pohlavie = ["samec","samica"] # list()
    velkost = .0 # float()
    
    # Chovanie/funkcie/metody/definicie (methods)
    def steka(self):
        print("Haf Haf")
        
    def lezi(self):
        print("Lezim a je mi dobre...")
        
    def vypis_info_vsetky(self):
        print("Je lenivy --> ", self.jeLenivy)
        print("Ako sa vola --> ", self.meno)
        print("Kolko ma rokov --> ", self.vek)

# Vytvorenie objektu Luigi typu Psik
luigi = Psik()
# Inicializacia vlastnosti/premmenych
luigi.meno = "Luigi"
luigi.vek = 1
luigi.jeLenivy = True
luigi.velkost = 32.6
luigi.steka()
luigi.steka()
luigi.lezi()
luigi.vypis_info_vsetky()

print("--------")
# Vytvor dalsi objekt
mario = Psik()
mario.meno = "Mario"
mario.vek = 2
mario.jeLenivy = False
print(mario.pohlavie[0])
mario.vypis_info_vsetky()


    



