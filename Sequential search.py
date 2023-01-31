def linear_search(alist,item):
    for pos in range(len(alist)):
        if alist[pos]==item:
            return True
    
    return False

def ordered_linear_search(alist,item):
    for pos in range(len(alist)):
        if alist[pos]==item:
            return True
        else:
            if alist[pos]>item:
                break
    
    return False
