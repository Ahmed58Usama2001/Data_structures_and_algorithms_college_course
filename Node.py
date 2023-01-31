class node:
    def __init__(self,initdata):
       self.data=initdata
       self.next=None

    def setdata(self,newdata):
        self.data=newdata
 
    def setnext(self,newnext):
        self.next=newnext

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

