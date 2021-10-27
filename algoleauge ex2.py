n = int(input())
a = [int(x) for x in input().split()]
result = 0
for i in range(len(a)):
    result += a[i]
result -= min(a)
print(result)