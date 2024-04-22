d,sumTime = input().split(' ')
d = int(d)
sumTime = int(sumTime)

if(d>=1 & d<=30 &sumTime>=0 & sumTime<=240):
    mins = 0
    maxs = 0
    minn = []
    maxn = []
    for i in range(d):
        a,b = input().split(' ')
        a = int(a)
        b = int(b)
        minn.append(a)
        maxn.append(b)
        mins += minn[i]
        maxs += maxn[i]
    if ((sumTime>=mins) & (sumTime<=maxs)):
        print("YES")
        j = 0
        p = 0
        values = 0
        result = []
        div = sumTime - mins
        for j in range(d):
            di = maxn[j] - minn[j]
            result.append(di)
        for p in range(d):
            if (div-result[p] <= 0):
                break
            div = div - result[p]

        k = 0
        m = 0
        for k in range(p):
            print(maxn[k],end=' ')
        print(minn[p]+div,end=' ')
        for m in range(p+1,d):
            print(minn[m],end=' ')
    else:
        print("NO")

else:
    print("False")


