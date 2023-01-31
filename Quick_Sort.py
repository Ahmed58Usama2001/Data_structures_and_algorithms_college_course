def quicksort(alist):
    quicksorthelper(alist,0,len(alist)-1)

def quicksorthelper(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)

        quicksorthelper(alist,first,splitpoint-1)
        quicksorthelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    done=False
    while not done:
       while leftmark<=rightmark and pivotvalue>=alist[leftmark]:
           leftmark=leftmark+1

       while rightmark>=leftmark and pivotvalue<=alist[rightmark]:
           rightmark=rightmark-1
       
       if leftmark>rightmark:
           done=True
       else:
           alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
    
    alist[rightmark],alist[first]=alist[first],alist[rightmark]
    return rightmark


alist=[5,77,22,9,0,12,74]
print(alist)
quicksort(alist)
print(alist)



