#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:41:28 2018

@author: alexs
"""

import numpy as np
np.random.seed(0)

x1 = np.random.randint(10, size=6) # One-dim array
x2 = np.random.randint(10, size=(3,4)) # Two-dim array
x3 = np.random.randint(10, size=(3,4,5)) # Three-dim array

print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)

print("dtype: ", x3.dtype)
print("itemsize: ", x3.itemsize, "bytes")
print("nbytes: ", x3.nbytes, "bytes")

print(x1)
print(x1[0])
print(x1[4])
print(x1[-1])
print(x1[-2])

print(x2)
print(x2[0,0])
print(x2[2,0])
print(x2[2,-1])

x2[0,0] = 12

print(x2[0,0])

print(x2)

x1[0] = 3.14159

print(x1)

x = np.arange(10)

print(x)
print(x[:5])
print(x[4:7])
print(x[::2])
print(x[1::2])
print(x[::-1])
print(x[5::-2])

print(x2[:2, :3]) # two rows, three columns
print(x2[:3, ::2]) # all rows, every other column
print(x2[::-1, ::-1]) # reverse array
print(x2[:, 0]) # first column of x2
print(x2[0, :]) # first row of x2
print(x2[0]) # equivalent to x2[0, :])

x2_sub = x2[:2, :2]
print(x2_sub)

x2_sub[0,0] = 99
print(x2_sub)
print(x2)

x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)

x2_sub_copy[0, 0] = 42
print(x2_sub_copy)
print(x2)

grid = np.arange(1,10).reshape((3,3))
print(grid)

x = np.array([1,2,3])
print(x)
print(x.reshape((1,3))) # row vector via reshape
print(x[np.newaxis, :]) # row vector via newaxis
print(x.reshape((3,1))) # column vector via reshape
print(x[:, np.newaxis]) # column vector via newaxis

