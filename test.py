# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:38:51 2019

additional comment

@author: marat
"""
s=input()
dic={}
for ch in s:
    if s in dic:
        dic[ch]+=1
    else:
        dic[ch]=1
        
for k, val in dic.item():
    print(k, val)
