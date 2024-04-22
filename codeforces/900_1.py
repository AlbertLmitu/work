s1 = input()
s2 = input()
i = -1
while(1):
    if((-i > len(s1)) | (-i > len(s2))):
        break
    if(s1[i] != s2[i]):
        break
    else:
        i = i-1
if(i==-1):
    print(len(s1)+len(s2))
else:
    print(len(s1)+len(s2)+2*i+2)

