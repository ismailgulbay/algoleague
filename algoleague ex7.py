def mid(bas, son):
    return (int(bas) + int(son)) // 2


def right(t):
    bas = 1
    son = n
    while son > bas:
        if t < costs[mid(bas, son) - 1]:
            son = mid(bas, son)
        else:
            bas = mid(bas, son) + 1
    return mid(bas, son)


def left(t):
    bas = 1
    son = n
    while son > bas:
        if t <= costs[mid(bas, son) - 1]:
            son = mid(bas, son)
        else:
            bas = mid(bas, son) + 1
    return mid(bas, son)


n, k = map(int, input().split())
costs = [int(x) for x in input().split()]
q = int(input())
for _ in range(q):
    t = int(input())
    print(right(k + t) - left(k - t) + 1)




