from dataStructures import *


def insert_linked_list(first_ll, second_ll, index):
    temp_ll=LinkedList()
    list1pointer=first_ll.get_head()
    list2pointer=second_ll.get_head()
    counter=0
    while list1pointer!=None :
          if counter==index:
             while list2pointer!=None:
                temp_ll.append(list2pointer.get_data())
                list2pointer=list2pointer.get_next()
          else:
           temp_ll.append(list1pointer.get_data())
           list1pointer=list1pointer.get_next()
          

          counter+=1
    
    return temp_ll


firstlist = LinkedList()
secondlist = LinkedList()
################
firstlist.add(4)
firstlist.add(3)
firstlist.add(2)
firstlist.add(7)
##################
secondlist.add(2)
secondlist.add(1)
##################

print("First")
firstlist.printList()
print("Second")
secondlist.printList()
print("_________")
firstlist = insert_linked_list(firstlist, secondlist,2)
firstlist.printList() # should print 7 2 1 2 3 4