class myqueue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
       return self.items==[]

    def enqueue (self,item):
        self.items.insert (0,item)

    def dequeue (self):
        return self.items.pop()

    def remove(self,i):
        self.items.pop(i)
    
    def size (self):
        return len(self.items)
