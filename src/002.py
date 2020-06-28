# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  002.py
@Description    :  
@CreateTime     :  2020-3-14 20:36
------------------------------------
@ModifyTime     :  
"""
import pandas as pd

# print(people.shape)
# print(people.columns)
# print(people.head(3))
# print("-----------------------")
# print(people.tail(4))
# people = pd.read_excel("F:/dataexcel/Temp/People - Copy.xlsx",header=None)
# people.columns = ["ID","Type","Title","FirstName","MiddleName","LastName"]
# people.set_index("ID",inplace=True)
# print(people.columns)
# people.to_excel("F:/dataexcel/Temp/output2.xlsx")
df = pd.read_excel("F:/dataexcel/Temp/output2.xlsx",index_col="ID")
df.to_excel("F:/dataexcel/Temp/output3.xlsx")
print("Done!")