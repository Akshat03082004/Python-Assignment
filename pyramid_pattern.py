# -*- coding: utf-8 -*-
"""Pyramid_pattern.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O6FNGC79wPZKClOuAMKCQKA8nyyUce0H
"""

for i in range(5,0,-1):
  for j in range(1,5-i+1):
    print(" ",end=" ")

  for k in range(1,i+1):
    print(" * ",end=" ")


  print()

for i in range(1,5):
  for j in range(i+1):
    print("*",end=" ")
  print()

for i in range(1,6):


    for j in range(6-i):
      print("*",end=" ")
    print()

for i in range(5):
  for k in range(5-i):
    print("*",end=" ")
  print()
for i in range(1,5):
  for j in range(0,i+1):
    print("*",end=" ")
  print()

for i in range(5,0,-1):
  for j in range(1,i+1):
    print("*",end=" ")
  print()

for i in range(1,5):
  for k in range(i+1):
    print("*",end=" ")
  print()

for i in range(1,6):
  for j in range(2,i+1):
    print(" ",end=" ")
  for k in range(i,6):
    print("*",end=" ")
  print()

for i in range(2,6):
  for j in range(i,5):
    print(" ",end=" ")
  for k in range(1,i+1):
    print("*",end=" ")
  print()