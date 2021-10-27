n = int(input())
lst = [int(x) for x in input().split()]
maks = lst[0]
sayac = 0
for i in range(len(lst)):
    if lst[i] > maks:
        maks = lst[i]
        sayac += 1
print(sayac)
