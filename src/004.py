# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  004.py
@Description    :  
@CreateTime     :  2020-3-16 13:32
------------------------------------
@ModifyTime     :  
"""
import pandas as pd
from datetime import date,timedelta

def add_month(d,md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd , m ,d.day)

books = pd.read_excel("F:/dataexcel/Temp/Books(1).xlsx",skiprows=3,usecols="C:F",dtype = {"ID":str,"InStore":str,"Date":str})
start = date(2018,1,1)
for i in books.index:
    books.at[i,"ID"] = i + 1
    books.at[i,"InStore"] = "Yes" if i % 2 == 0 else "No"
    books.at[i,"Date"] = add_month(start,i)
    # books["ID"].at[i] = i + 1
    # books["InStore"].at[i] = "YES" if i % 2 == 0 else "NO"
    # books["Date"].at[i] = start + timedelta(days=i)
    # books["Date"].at[i] = date(start.year + i, start.month ,start.day)
    # books["Date"].at[i] = add_month(start , i)
print(books)
books.set_index("ID",inplace=True)
books.to_excel("F:/dataexcel/Temp/output_books2.xlsx")
