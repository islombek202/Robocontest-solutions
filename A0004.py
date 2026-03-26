n = int(input())
sonlar = list(map(int, input().split()))
yolgiz_son = 0
for x in sonlar:
    yolgiz_son = yolgiz_son ^ x
print(yolgiz_son)