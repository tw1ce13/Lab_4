from pyDatalog import pyDatalog
from random import randint

pyDatalog.create_terms('X, Sum, Average, median, Median, arr, mult, Mult')

# Сумма ряда
Sum[X] = ((1 + X) * X) / 2
print("Sum 1-999999:")
print(Sum[999999] == X)

# Среднее арифметическое
Average[X] = X / 2
print("Average 1-999999: ")
print(Average[999999] == X)

# Медиана
for i in range(100):
    arr[i] = randint(1,100)
arr.sort()
median[X] = arr[X // 2]
print(median[100] == Median)

# Произведение
mult[X] = X * mult[X - 1]
mult[1] = 1
print(mult[100] == Mult)

