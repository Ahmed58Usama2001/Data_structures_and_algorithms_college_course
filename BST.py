class bst:
    def __init__(self):
        self.root=None
        self.size=0

    def size(self):
        return self.size
    
    def bstsearch(self,subtree,target):
        if subtree is None:
            return None
        elif target<subtree.key:
            return self.bstsearch(subtree.left,target)
        elif target>subtree.key:
            return self.bstsearch(self.right,target)
        else:
            return subtree

    def has_key(self,key):
        return self.bstsearch(self.root,key) is not None

    def valueof(self,key):
        node=self.bstsearch(self.root,key)
        assert node is not None,"Invalid key"
        return node.value

    def bstminimum(self,subtree):
        if subtree is None:
            return None
        else:
            if subtree.left is None:
                return subtree
            else:
                return self.bstminimum(subtree.left)

    def bstmaximum(self,subtree):
        if subtree is None:
            return None
        else:
            if subtree.right is None:
                return subtree
            else:
                return self.bstmaximum(subtree.right)            

    def add(self,key,value):
        node=self.bstsearch(self.root,key,value)
        if node is not None:
            node.value=value
            return False
        else:
            self.root=self.bstinsert(self.root,key,value)
            self.size+=1
            return True

    def bstinsert(self,subtree,key,value):
        if subtree is None:
            subtree=bstnode(key,value)
        elif key<subtree.key:
            subtree.left=self.bstinsert(subtree.left,key,value)
        else:
            subtree.right=self.bstinsert(subtree.right,key,value)
        return subtree

    def remove(self,key):
        node=self.bstsearch(self.root,key)
        assert node is not None,"Invalid value"
        self.root=self.bstremove(self.root,key)
        self.size-=1

    def bstremove(self,subtree,target):
        if target>subtree.key:
            subtree.right=self.bstremove(subtree.right,target)
            return subtree
        elif target<subtree.key:
            subtree.left=self.bstremove(subtree.left,target)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor=self.bstminimum(subtree.right)
                subtree.key=successor.key
                subtree.value=successor.value
                subtree.right=self.bstremove(subtree.right,successor.key)
                return subtree






class bstnode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None

        