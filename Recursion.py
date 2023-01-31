def printrev(n):
    print(n)
    if n>0:
        printrev(n-1)
printrev(4)


def printinc(n):
    if n>=0:
        printinc(n-1)
        print(n)
printinc(4)


alist=[5,6,33,80]
def listsum(alist):
    if len(alist)==1:
        return alist[0]
    else:
        return alist[0]+listsum(alist[1:])

print(listsum(alist))
