n1 = int(input())
L1= [int(x) for x in input().split()]
st = set(L1)
for x in st :
    if L1.count(x)==1 :
        print(x,end='')
        break
