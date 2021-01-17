# -*- coding: utf-8 -*-
"""
Practice code written while completing exercise 3.

Created on Thu Dec 31 13:24:21 2020

@author: nathan.m
"""
firstset =[9]
testset = firstset[0]
subset = [1,2,3]
next_subset = subset[:] + [testset]
print(next_subset)