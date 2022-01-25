# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:16:34 2022

@author: Administrator
"""

class Zakaznik(object):
    """Zakaznik banky XYZ, ktory ma sporiaci ucet.
    Zakaznici maju nasledovne vlastnosti:
    Vlastnosti:
    meno - string - meno zakaznik
    zostatok - int - fin. zostatok na ucte
    """
    def __init__(self, meno, zostatok = 0):
        """Vrati objekt typu zakaznik, ktory ma meno a zostatok"""
        self.name = meno
        self.zostatok = zostatok
    
    def vklad(self, ciastka):
        """Vrati zostatok upraveny o ciastku"""
        self.zostatok = self.zostatok + ciastka
        # self.zostatok += ciastka
        return self.zostatok
    
    def vyber(self, ciastka):
        """Vybrat len tolko na penazi kolko mate na ucte"""
        if ciastka > self.zostatok:
            raise RuntimeError("Ciastka, ktoru vyberas je vacsia ako zostatok")
        self.zostatok = self.zostatok - ciastka
        # self.zostatok -= ciastka
        return self.zostatok 
        

prvy_zakaznik = Zakaznik("Ivan")
druhy_zakaznik = Zakaznik("Maria", 350)

prvy_zakaznik.vklad(3000)
# prvy_zakaznik.vyber(5000)

druhy_zakaznik.vyber(350)
