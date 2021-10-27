n = int(input())
a = input()
b = ''
for i in range(len(a)):
    if i + 1 != len(a):
        if a[i] == a[i + 1]:
            continue
        else:
            b += a[i]
    else:
        b += a[i]
print(b)
