# -*- coding: utf-8 -*-
"""21_04_2023_3potok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hKIx37psGn6eVKOX_j1KQX6GNQ1bf2jn
"""

a = float(input("Введи делимое: "))
b = float(input("Введи делитель: "))

try:
  x = a / b
  print(x)  
except ZeroDivisionError:
  print("На ноль делить нельзя!!!")
finally:
  print("Сработал блок файнали")

import random
x = random.randint(0,10)
print(x)

import random

arr = [1,2,3,4,5,"Tect1","Tect2","tect3"]
#print("Случайное значение: ",random.choice(arr))
#print(len(arr))
print(type(arr))

import random
y = random.random()
print(type(y))

x = "Привет"
print(type(x))

x = "Привет"
print(len(x))

import random
y = random.uniform(1.5,2.5)
print(y)

import random
a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
d = random.randint(1,6)
total = a + b + c + d

print("Бросок 1",a,"Бросок 2",b,"Бросок 3",c,"Бросок 4",d)
print("Общая сумма",total)

import random

k = 4
y = []

while k != 0:
  x = random.randint(1,6)
  k -= 1
  y .append(x)
  print(y)

print ("Суммарное значение 4 бросков",sum(y))

import random

k = 4
y = []
total = 0

while k != 0:
  x = random.randint(1,6)
  k -= 1
  y .append(x)
  print(y)

for i in y:
  print("Значение i",i,"Значение total",total)
  total += i

print ("Суммарное значение 4 бросков",total)