## Calculator
from math import log, exp
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