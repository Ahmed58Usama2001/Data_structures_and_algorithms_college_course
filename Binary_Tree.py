class binarytree:
    def __init__(self,rootobj) :
       self.key=rootobj
       self.left=None
       self.right=None

    def insertleft(self,newnode):
        if self.left==None:
            self.left=binarytree(newnode)
        else:
            t=binarytree(newnode)
            t.left=self.left
            self.left=t

    def insertright(self,newnode):
        if self.right==None:
            self.right=binarytree(newnode)
        else:
            t=binarytree(newnode)
            t.right=self.right
            self.right=t

    def setrootval(self,obj):
        self.key=obj
    
    def getrootval(self):
        return self.key

    def getleftchild(self):
        return self.left
    
    def getrightchild(self):
        return self.right
