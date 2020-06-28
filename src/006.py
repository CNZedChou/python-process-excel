# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  006.py
@Description    :  
@CreateTime     :  2020-3-16 14:21
------------------------------------
@ModifyTime     :  
"""
import pandas as pd
products = pd.read_excel("F:/dataexcel/Temp/List.xlsx",index_col="ID")
# products.sort_values(by = "Price",inplace=True,ascending=False)
products.sort_values(by = ["Worthy","Price"],inplace=True,ascending=[True,False])
print(products)
