
class printer:
    def __init__( self , pages ):
       self.pagerate= pages
       self.currentTask=None
       self.timeRemaining=0

    def tick (self):
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining==0:
                self.currentTask=None
    
    def busy (self):
        if self.currentTask!=None:
         return True
        else:
            return False

    def startNext (self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()\
            * 60/self.pagerate


