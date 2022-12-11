import math
import matplotlib.pyplot as plt
import sys
import numpy as np
from scipy.linalg import solve


#sys.stdout = open("result2lab.txt", "w")
def setData(fileName, data):
    file = open(fileName, 'r')
    for line in file:
        data.append(int(line.strip()))

data =[]
setData("input_100.txt",data)
print("Послідовність:", data)
#-1-----------------------------------------------
print('Task 1')
def task1(num):
    index = num * (lens + 1) - 1
    result = data[int(index)] + (index % int(index)) * (data[int(index) + 1] - data[int(index)])
    return result

lens = len(data)

Q1 = task1(1 / 4)
Q3 = task1(3 / 4)
P9 = task1(0.9)
print("\nQ1 = ", Q1)
print("\nQ3 = ", Q3)
print("\nP90 = ", P9)
#-----------------------------------------------
#2----------------------------------------------
print('Task 2')
def Task2():
    sum = 0
    totalsum = 0
    totalSum = 0
    for i in range(lens):
        sum += data[i]
    for i in range(lens):
        totalsum += (data[i] - (sum / lens)) ** 2
        totalSum += abs(data[i] - (sum / lens))

    result = totalsum / lens
    Result = totalSum / lens
    print("Стандартне відхилення = ", str(round(math.sqrt(result))))
    print("Середнє відхилення = ", str(round(Result)))

Task2()
#-----------------------------------------------
#3----------------------------------------------
print(" ")
print("Task 3")

a = (25/129)
b = (10400/129)

for i in range(len(data)):
    y = a * data[i] + b
    print(data[i], int(y))
    data[i] = y
#----------------------------------------------
#4---------------------------------------------
stems = [i for i in range(101)]
plt.xlim(0, 101)
plt.stem(stems, data)
plt.show()
#----------------------------------------------
#5---------------------------------------------
plt.boxplot(data)
plt.show()

#----------------------------------------------
#sys.stdout.close()