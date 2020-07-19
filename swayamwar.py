
n=int(input())
girl=input()
boy=input()
f=0
for i in range(n):
    if girl[i] in boy:
        j=boy.index(girl[i])
        boy=boy[:j]+boy[j+1:]
    else:
        print(len(boy))
        f=1
        break
if(f==0):
    print(0)
