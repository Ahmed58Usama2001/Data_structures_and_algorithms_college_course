
import operator
from Binary_Tree import*
def evaluate (prasetree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftc=prasetree.getleftchild()
    rightc=prasetree.getrightchild()
    if leftc and rightc :
        fn=opers[prasetree.getrootval()]
        return fn(evaluate(leftc),evaluate(rightc))
    else:
        return (prasetree.getrootval())
