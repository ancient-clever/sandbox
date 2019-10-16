n = int(input())
l = []

for r in range(1, n+1):
    while l.count(r) != r and len(l) != n:
        l.append(r)
for i in l:
    print(i, end=' ')
