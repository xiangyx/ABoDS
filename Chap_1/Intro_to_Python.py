## Calculator
from math import log, exp, sqrt
print(log(exp(1)))
exp(1)

## Variable & Type
a = 2
b = 5.0
x = "Hello World"
print(a)
print(b)
print(x)

c = 2 * a + b
print(c)

print(type(x))
print(type(c))

## Functions
def fun1(x):
    return x**x
print(fun1(2))

def fun2():
    print("Input and output are not needed here.")
fun2()

def fun3(x, base = 2):
    return log(x, base)
print(f"base {10}: {fun3(10, 10)}")
print("base {}: {}".format(exp(1).__round__(4), fun3(exp(1), exp(1))))
print(f"base {2}: {fun3(2, base = 2)}")

def fun4(x):
    if x >= 0:
        return x
    else:
        return -x
print(fun4(10))
print(fun4(-10))

def fun5(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"
print(fun5(10))
print(fun5(-10))
print(fun5(0))

# For loop
for i in range(1, 4):
    print(i)

print(type(range(1, 4)))

# While loop
i = 1
while i <= 3:
    print(i)
    i += 1
print("-------\n")

# Contibue/Break

for i in range(1, 4):
    if i == 2: continue
    print(i)

print("-------\n")
for i in range(1, 4):
    if i == 2: break
    print(i)
print("-------\n")

# Built-in Data Structures-------------------------------
## Lists
x = list(range(4))
y = ["Another Hello World!"]
print(len(x))
print(len(y))
print([l.split(" ") for l in y])
print(x[-1])
print(x[len(x) - 1])

print(x * 5)
print([0, 1] * 5)

# Point to the same memory address
x = [0]
y = [x] * 5
print(y)
y[2] = 2
print("x:", x)
print("y:", y)
y[0][0] = 3
print("x:", x)
print("y:", y)
print("------")
# Point to different memroy address
x = [0]
y = [x[:] for _ in range(5)]
print(y)
y[2] = 2
print("x:", x)
print("y:", y)
y[0][0] = 3
print("x:", x)
print("y:", y)
print("---------------")
# List comprehension
x = list(range(20))
print([e for e in x if e % 2 == 0])
print([e for e in x if int(sqrt(e))**2 == e])
print([e**2 if e % 2 == 0 else -1 for e in x])
print("----------------")
# Some list operations
x = [1, 2, 3]
y = [5, 6]
# append a single value
x.append(4)
print(x)
# concatenate two lists
x.extend(y)
print(x)
# Remove the last element
x.pop()
print(x)
print("--------------")

# Array
import numpy as np
array1 = np.reshape(list(range(1, 10)), (3, 3), order = "F")
print(array1)
array2 = np.reshape(list(range(1, 7)), (3, 2), order = "F")
print(array2)
print(np.dot(array1, array2))
x = np.array(list(range(1, 4)))
print(x + 1)
print("--------------")
# Data-frame
import pandas as pd
df1 = pd.DataFrame({'names':['A', 'B', 'C'], 'age':[10, 25, 37]})
print(df1)
x = np.random.normal(size=(3, 3))
print(x)
x = pd.DataFrame(x)
print(x)
x = np.asarray(x)
print(x)
print("--------------")