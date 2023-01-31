
def preorder(tree):
    if tree!=None:
        print(tree.getrootval())
        preorder(tree.getleftchild())
        preorder(tree.getrightchild())

def postorder(tree):
    if tree!=None:
        postorder(tree.getleftchild())
        postorder(tree.getrightchild())
        print(tree.getrootval())

def inorder(tree):
    if tree!=None:
        inorder(tree.getleftchild())
        print(tree.getrootval())
        inorder(tree.getrightchild())