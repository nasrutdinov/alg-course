# -*- coding: utf-8 -*-
"""
Сортировка слиянием

@author: mfn
"""

#слияние списков
def merge(A:list, B:list):
    C=[0]*(len(A)+len(B))
    i=j=n=0
    while i<len(A) and j<len(B):
        if A[i]<=B[j]:
            C[n]=A[i]
            i+=1
            n+=1
        else:
            C[n]=B[j]
            j+=1
            n+=1
    while i<len(A):
        C[n]=A[i]
        i+=1
        n+=1
    while j<len(B):
        C[n]=B[j]
        j+=1
        n+=1
    return C

#сортировка
def sort_merge(A):
    if len(A)<2:
        return
    k=len(A)//2
    R=[]
    L=[]
    for i in range(0,k):
        L.append(A[i])
    for i in range(k,len(A)):
        R.append(A[i])
    #print("***************")
    #print(L)
    #print(R)
    
    sort_merge(L)
    sort_merge(R)
    C=merge(L,R)
    #print(C)
    for i in range(0,len(C)):
        A[i]=C[i]
    #print(A)
    #return

    
A=[3,4,2,1,4,6,7,2,3]

#print(merge([3,4,5,6],[2,6,7,8,9]))
sort_merge(A)
print(A)
    
