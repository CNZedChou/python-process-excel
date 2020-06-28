# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  005.py
@Description    :  
@CreateTime     :  2020-3-16 14:10
------------------------------------
@ModifyTime     :  
"""
import pandas as pd
# def add_2(x):
#     return x + 2
books = pd.read_excel("F:/dataexcel/Temp/Books_func.xlsx",index_col="ID")
# books["Price"] = books["ListPrice"] * books["Discount"]
# for i in books.index:
# #     books["Price"].at[i] = books["ListPrice"].at[i] * books["Discount"].at[i]
# books["ListPrice"] = books["ListPrice"].apply(add_2)
books["ListPrice"] = books["ListPrice"].apply(lambda x : x + 2)
print(books)
