from Printer import *
from task import *
from Myqueue import *
import random

def simulation (numseconds,pagesperminute):
      labprinter=printer(pagesperminute)
      printqueue=myqueue()
      waitingtimes=[]

      for currentsecond in range(numseconds):
          if random.randrange(1,181)==180 :
             task =Task(currentsecond)
             printqueue.enqueue(task)

          if(not labprinter.busy())and(not printqueue.isEmpty()):
                 nexttask=printqueue.dequeue()
                 waitingtimes.append(nexttask.waitTime(currentsecond))
                 labprinter.startNext(nexttask)
          
          labprinter.tick()

      averageWait=sum(waitingtimes)/len(waitingtimes)
      print ("Average Wait " , averageWait ," secs" ,printqueue.size() , " tasks remaining.")

