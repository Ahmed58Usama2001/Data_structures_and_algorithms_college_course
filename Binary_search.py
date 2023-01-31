def binarysearch(alist,key):
    first=0
    last=len(alist)-1
    while first<=last:
        midpoint=(first+last)//2
        if alist[midpoint]==key:
            return True
        elif alist[midpoint]>key:
            last=midpoint-1
        elif alist[midpoint]<key:
            first=midpoint+1

    return False

def recursive_binarysearch(alist,key):
    if len(alist)==0:
       return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==key:
            return True
        else:
            if alist[midpoint]>key:
                return recursive_binarysearch(alist[:midpoint],key)
            else:
                return recursive_binarysearch(alist[midpoint+1:],key)
