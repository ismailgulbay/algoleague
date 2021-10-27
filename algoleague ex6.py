def calculate(x):
    temp = 1
    while (x > 0):
        if x % 10 != 0:
            temp *= x % 10
        x //= 10

    return temp


n = int(input())

while (n >= 10):
    n = calculate(n)
print(n)