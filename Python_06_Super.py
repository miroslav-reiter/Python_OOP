# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:35:21 2022

@author: Administrator
"""

class Psik:
    meno = ""
    vek = 0
    farba_srst = ""
    hlasitost = 0
    
    def steka(self, hlasitost):
        return f"{self.meno} steka o hlasitosti: {hlasitost}"
    
    def __init__(self, meno = "Oriesok"):
        self.meno = meno

class Spic(Psik):
    farba_srst = "svetlo kremova"
    hlasitost = 50

class Pomik(Psik):
    hlasitost = 15
    def steka(self, hlasitost = 10):
        return super().steka(16)

prvy_psik = Psik("Luigi")
print(prvy_psik.steka(30))

prvy_psik.meno = "Luigi"
print(prvy_psik.steka(20))

prvy_spic = Spic()
print(prvy_spic.hlasitost)
print(prvy_spic.steka(10))

prvy_pomik = Pomik()
print(prvy_pomik.hlasitost)
print(prvy_pomik.steka(32))