def insertionsort(alist):
    for index in range(1,len(alist)):

        currentvalue=alist[index]
        position=index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue



alist=[5,77,22,9,0,12,74]
print(alist)
insertionsort(alist)
print(alist)