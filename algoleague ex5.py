def hesap(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return hesap(n - x) + hesap(n - y)



n = int(input())
x,y = map(int,input().split())
print(hesap(n))