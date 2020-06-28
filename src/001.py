# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  001.py
@Description    :  
@CreateTime     :  2020-3-14 19:30
------------------------------------
@ModifyTime     :  
"""
import pandas as pd
df = pd.DataFrame({"ID":[1,2,3],"Name":["Tim","Vic","Nick"]})
df = df.set_index("ID")
print(df)
df.to_excel("F:/dataexcel/output.xlsx")
print("done!")