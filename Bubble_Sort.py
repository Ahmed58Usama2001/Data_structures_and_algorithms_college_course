def bubblesort(alist):
    n=len(alist)
    for passnum in range(n-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
    
alist=[5,77,22,9,0,12,74]
print(alist)
bubblesort(alist)
print(alist)


def smartbubblesort(alist):
    n=len(alist)
    exchanges=True
    for passnum in range(n-1,0,-1):
        if exchanges==False:
            break
        exchanges=False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                exchanges=True
