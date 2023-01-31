from Binary_Tree import *
from Evaluate import *
from Parse_Tree import *
from Tree_Traversals import *
r = binarytree('a')
print(r.getrootval( ) )
print(r.getleftchild( ))
r.insertleft('b')
print(r.getleftchild( ).getrootval( ) )
r.insertright('c')
print(r.getrightchild( ).getrootval( ))
r.getrightchild( ).setrootval('hello')
print(r.getrightchild( ).getrootval( ))



pt = buildparsetree("( ( 10 + 5 ) * 3 )") 
print (evaluate(pt))
print(preorder(pt))
print(postorder(pt))
print(inorder(pt))