# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  003.py
@Description    :  
@CreateTime     :  2020-3-14 21:29
------------------------------------
@ModifyTime     :  
"""
# import pandas as pd
# s1 = pd.Series()
# d = {"X":100,"Y":200,"Z":300}
# s1 = pd.Series(d)
# print(s1)
# print(s1.index)
# print(s1.data)
# import pandas as pd
# L1 = [100,200,300]
# L2 = ["X","Y","Z"]
# s1 = pd.Series(L1,index=L2)
# print(s1)
# print(s1.index)
import pandas as pd
s1 = pd.Series([1,2,3],index=[1,2,3],name="A")
s2 = pd.Series([10,20,30],index=[1,2,3],name="B")
s3 = pd.Series([100,200,300],index=[2,3,4],name="C")

df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
# df = pd.DataFrame([s1,s2,s3])
print(df)