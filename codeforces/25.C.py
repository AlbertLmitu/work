def find(a):
    l = 0
    for l in range(len(a)):
        if (a[l] == min(a)):
            c = a.pop(l)
            return l

t = int(input())
p = 0
values = []
for p in range(t):
    n,m,k = input().split(' ')
    n = int(n)
    m = int(m)
    k = int(k)
    a = []
    z = 0
    a = list(input().split(' '))
    for z in range(n):
        a[z] = int(a[z])
    b = a.copy()
    mark = []

    while(k>m):
        mark.append(find(a))
        k = k-m

    M = find(a)

    j = 0
    value = 0
    for j in range(n):
        if(j in mark):
            value = value + m*b[j]
            b = list(map(lambda x: x + m, b))
        if(j==M):
            value = value + k*b[j]
            b = list(map(lambda x: x + k, b))
    values.append(value)
f = 0
for f in range(t):
    print(values[f])


