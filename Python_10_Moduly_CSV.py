# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:09:34 2022

@author: Administrator
"""

import os
import pandas as pd

# dataframe1 = pd.read_csv("products.csv")
# print(dataframe1)

writer = pd.ExcelWriter("company_data.xlsx", engine="xlsxwriter")
writer.close()