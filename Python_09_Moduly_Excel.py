# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:36:36 2022

@author: Administrator
"""

import os
import pandas as pd
import sys

# Current work directory
cwd = os.getcwd()
print("Aktualny pracovny priecinok -->", cwd)
print("\nZoznam suborov:")
print(os.listdir())

file = "company_data.xlsx"
excel = pd.ExcelFile(file)
print(excel.sheet_names)
dataframe1 = excel.parse("Hárok2")
print(dataframe1)

dataframe1.to_csv("")

excel.close()
del excel

