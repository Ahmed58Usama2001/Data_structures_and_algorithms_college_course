from dataStructures import *
def BottomInsert(s, value):
   
    if s.isEmpty():
         
        
        s.push(value)
         
   
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

def Reverse(s): 
    if s.isEmpty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)

def remove_kth_from_stack(input_stack, k):
    temp_stack=Stack()
    target=input_stack.size()-1-k
    for i in range(input_stack.size()):
      if i==(target):
          input_stack.pop()
      else:
           token=input_stack.pop()
           temp_stack.push(token)
       
    Reverse(temp_stack)
 
    
    return temp_stack


mystack = Stack()

mystack.push(1)
mystack.push(5)
mystack.push(7)
mystack.push(8)
mystack.push(9)

mystack.printStack()

mystack = remove_kth_from_stack(mystack, 1)

mystack.printStack()  # this should print [1, 7, 8, 9]
