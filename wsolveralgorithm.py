f=open("freqdict.txt","r")
g=eval(f.read())
b=[h for h in g]
a="crane"
for x in range(6):
    print(a)
    c=[]
    while True:
        d=input("Enter guess code: ")
        for i in range(5):
                if d[i]=="g":
                    c+=["g"+a[i]+str(i)]
                elif d[i]=="y":
                    c+=["y"+a[i]+str(i)]
                elif d[i]=="a":
                    c+=["a"+a[i]+str(i)]
                else:
                    print("Entered status is not valid.")
                    break
        else: break
    c=sorted(c)
    for y in range(len(b)):
        d=[]
        for z in range(len(c)):
            if c[z][0] in 'gy':
                if not c[z][1] in b[y]:
                    b[y]=''
                    break
                elif c[z][0]=='g' and not c[z][1]==b[y][int(c[z][2])]:
                    b[y]=''
                    break
                elif c[z][0]=='y' and c[z][1]==b[y][int(c[z][2])]:
                    b[y]=''
                    break
            else:
                if c[z][1] in b[y] and b[y].count(c[z][1])>d.count(c[z][1]):
                    b[y]=''
                    break
            d+=[c[z][1]]
    b=list(set(b))[1::]
    e=[b[0]]
    for y in b[1::]:
        for z in range(len(e)):
            if(g[y]<=g[e[z]]):
                e.insert(z,y)
                break
        else:
            e+=[y]
    a=e[-1]
f.close()
