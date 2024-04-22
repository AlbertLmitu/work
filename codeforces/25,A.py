t = int(input())
p = 0
g = []
for p in range(t):
    n,k = input().split(' ')
    n = int(n)
    k = int(k)
    a = []
    m = 0
    o = 0
    q = 0

    a = list(input().split(' '))
    j = 0
    for j in range(k):
        if(int(a[j]) > int(a[k-1])):
            m = m + 1
            if(m==1):
                b1 = j+1
            if(m==2):
                b2 = j+1
                break

    if(m==1):
        if((k-b1)>(b1-2)):
            oput =k-b1
        else:
            oput = b1-2
    if (m == 2):
        if ((b2 - b1) > (b1 - 2)):
            oput = b2 - b1
        else:
            oput = b1 - 2
    if (m == 0):
        for o in range(k,t):
            if(a[o]>a[k-1]):
                q = o+1
                break
        if(q == 0):
            oput = n-1
        else:
            oput = q-2

    g.append(oput)
f = 0
for f in range(t):
    print(g[f])




