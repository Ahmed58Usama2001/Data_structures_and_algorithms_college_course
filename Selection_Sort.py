def selectionsort(alist):
    n=len(alist)
    for i in range(n-1):
        min=alist[i]
        minposition=i
        for j in range(i+1,n):
            if alist[j]<min:
                min=alist[j]
                minposition=j
        alist[i],alist[minposition]=alist[minposition],alist[i]

alist=[5,77,22,9,0,12,74]
print(alist)
selectionsort(alist)
print(alist)
