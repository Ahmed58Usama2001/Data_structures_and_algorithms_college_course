def mergesort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1

            else :
                alist[k]=righthalf[j]
                j=j+1
            
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        
    return alist

alist=[5,77,22,9,0,12,74]
print(mergesort(alist))