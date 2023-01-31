from Node import *

class unorderedlist:
    def __init__(self):
        self.head=None

    def isempty(self):
        return self.head==None

    def add(self,item):
        temp=node(item)
        temp.setnext(self.head)
        self.head=temp

    def length(self): #traversing from the head to the end
        current=self.head
        counter=0
        while current!=None:
            counter=counter+1
            current= current.getnext()
        return counter

    def search(self,item): #traversal search
        current=self.head
        while current!=None:
            if current.getdata()==item:
                return True
            else:
                current=current.getnext()

        return False

    def remove(self,item):
        previous=None
        current=self.head
        found=False
        while not found:
            if current.getdata()==item:
                found=True
            else:
                previous=current
                current=current.getnext()
        if previous==None:
            self.head=current.getnext()
        else:
            previous.setnext(current.getnext())


    def printll(self):
        current=self.head
        while current != None:
            print(current.getdata())
            current=current.getnext()
    
    
    