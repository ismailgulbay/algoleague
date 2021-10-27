lst = [int(x) for x in input().split()]
n = lst[0]
k = lst[1]
harfler = input()
harun = 0
sami = 0
for x in range(len(harfler)):
    if harfler[x] == 'H':
        harun += 1
    elif harfler[x] == 'S':
        sami += 1
if harun > n / 2:
    print("Harun")
elif sami > n / 2:
    print("Sami")
else:
    print("Cilek")
