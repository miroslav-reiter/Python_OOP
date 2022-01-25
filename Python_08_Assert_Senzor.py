# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:49:16 2022

@author: Administrator
"""

class Senzor:
    
    def prevod_kelvin_fahrenheit(self, teplota):
        assert (teplota >= 0), "Menej ako absolutna 0!"
        return ((teplota-273)*1.8)+32

prvy_senzor_tesla = Senzor()
# print(prvy_senzor_tesla.prevod_kelvin_fahrenheit(100))
# print(prvy_senzor_tesla.prevod_kelvin_fahrenheit(-100))

print(isinstance(prvy_senzor_tesla, Senzor))
print(isinstance(prvy_senzor_tesla, str))
print(isinstance(prvy_senzor_tesla, int))
print(isinstance(prvy_senzor_tesla, object))
print(isinstance("Adam Sangala", str))
print(isinstance(42, int))

print(issubclass(Senzor, Senzor))
print(issubclass(Senzor, object))
print(issubclass(Exception, object))
print(issubclass(EnvironmentError, object))