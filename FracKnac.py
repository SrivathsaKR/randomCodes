# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:54:15 2019

@author: MAHE
"""

# Fractional Knapsack


def BestItem(W, V,RemAmt):
    MaxValPerWt = 0
    Best = 0
    for i in range(1,len(W)):
        if RemAmt[i] > 0:
            if float(V[i]/W[i]) > MaxValPerWt:
                MaxValPerWt = float(V[i]/W[i])
                Best = i
    return Best

def FracKnac(W, V, RemCap):
    Amt = []
    RemAmt = W
    for x in range(len(W)):
        Amt.append(0)
    TotalValue = 0
    
    for j in range(1, len(W)+1):
     if RemCap == 0:
         return TotalValue,Amt
     i = BestItem(W, V,RemAmt)
     a = min((RemCap,RemAmt[i]))
     TotalValue += a * V[i]/W[i]
     RemCap -= a
     Amt[i] +=  a 
     RemAmt[i] -= a
    return TotalValue,Amt

W = [0]
V = [0]
n = int(input("Enter no of Items :"))
Rem = int(input("Total Capacity of Knapsack :"))
for i in range(1,n+1):
    W.append(int(input("Enter total weight of item {} :".format(i))))
    V.append(int(input("Enter total value of item {} :".format(i))))
print("Weight List : ",W[1:])
print("Value List : ",V[1:])
TotValue,Amt = FracKnac(W ,V, Rem) 
print("Result : Total value : {} Amount array : {} ".format(TotValue,Amt[1:]))