from Stack import *
from Binary_Tree import *
def buildparsetree(fpexp):
    fplist=fpexp.split()
    etree=binarytree(' ')
    pstack=stack()
    pstack.push(etree)
    currenttree=etree
    for token in fplist:
        if token =='(':
            currenttree.insertleft(' ')
            pstack.push(currenttree)
            currenttree=currenttree.getleftchild()
        elif token not in '+-*/)':
            currenttree.setrootval(int(token))
            currenttree=pstack.pop()
        elif token in '+=*/':
            currenttree.setrootval(token)
            currenttree.insertright(' ')
            pstack.push(currenttree)
            currenttree=currenttree.getrightchild()
        elif token == ')':
            currenttree=pstack.pop()
        else:
            print("error: i cannot recognize" + token)
   
    return etree
