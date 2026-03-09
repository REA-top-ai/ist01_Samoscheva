#Задание 1
##iterr
def factorial(n):
    if n < 0:
        return False
    elif n == 0:
        return 1
    x = 1
    for i in range(1, n+1):
        x *= i
    return x
print(factorial(0))

##recur
def factorial1(n):
    if n < 0:
        return False
    elif n == 0:
        return 1
    return n * factorial1(n-1)
print(factorial1(5))

#задание 2
def square(n):
    numbers = []
    for x in n:
        numbers.append(x**2)
    return numbers
print(square([2,3,4,5,6]))

def square1(n):
    numbers = []
    if len(n) == 0:
        return numbers
    else:
        x = numbers[0]**2 + square(n[1:])
        return x
print(square([6,5,4,3,2]))







