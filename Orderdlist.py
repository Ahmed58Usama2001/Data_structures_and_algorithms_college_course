from Node import *

class orderedlist:
    def __init__(self):
      self.head=None

    def isempty(self):
        return self.head==None

    def length(self): #traversing from the head to the end
        current=self.head
        counter=0
        while current!=None:
            counter=counter+1
            current=current.getnext()
        return counter

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

    def search(self,item): #traversal search
         current=self.head
         while current!=None:
            if current.getdata()==item:
                return True
            else:
                if current.getdata()>item:
                    break
                else:
                    current=current.getnext()
         return False

    def add(self,item):
        temp=node(item)
        previous=None
        current=self.head
        while current!=None:
            if current.getdata()>item:
                break
            else:
                previous=current
                current=current.getnext()
        if previous ==None:
            temp.setnext(current) 
            #temp.setnext(self.head)
            self.head=temp
        else:
            temp.setnext(current)
            previous.setnext(temp)
            
