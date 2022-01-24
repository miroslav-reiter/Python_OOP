# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:11:57 2022

@author: Administrator
"""

class Macicka:
    rasa = "perzska"
    def __init__(self, m, v):
        """m - meno
           v - vek (celecislo)
        """
        self.m = m
        self.v = v
        
salem = Macicka("Salem", 500)
murko = Macicka("Murko", 3)

print(salem.v)
print(salem.rasa)
print(murko.v)
print(murko.rasa)
