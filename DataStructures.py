"""
Data Structures

1) Stacks
2) Singly Linked Lists
3) Doubly Linked Lists
4) Queues
5) Trees
5) Graphs
6) Heaps

"""

class PriorityQueue(object):

    def __init__(self):
        self.lst = []
        self.priority = None
    def 
    
class Stack(object):
    def __init__(self,lst=[]):
        self.lst = lst
        self.length = 0
    def push(self,entity):
        self.lst.append(entity)
        self.length = self.length + 1
    def pop(self):
        if self.length == 0:
            return False
        else:
            self.length = self.length - 1
            return self.lst.pop(self.length)
    def returnStack(self):
        return self.lst
    def length(self):
        return self.length

######################################     
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def __str__(self):
        return self.value

######################################    
class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
        
    def insert(self,value):
        self.node = Node(value)
        self.node.next = self.head
        self.head = self.node
        
    def remove(self,value=None):
        if self.head == None:
            return False
        else:
            if value == None:
                self.head = self.head.next
            else:
                tempNode = self.head
                count = 0
                while tempNode != None:
                    count = count + 1
                    if tempNode.next.getValue() == value:
                        tempNode.next = tempNode.next.next
                        break
                    else:
                        tempNode = tempNode.next
        
        
    def contains(self,value):
        tempNode = self.head
        while tempNode != None:
            if tempNode.getValue() == value:
                return True
                break
            else:
                tempNode = tempNode.next
        return False
    def traverse(self):
        tempNode = self.head
        while tempNode != None:
            print tempNode.getValue()
            tempNode = tempNode.next
######################################
class Queue(object):
    def __init__(self):
        self.list = []

    def queue(self,entity):
        self.list.append(entity)
    def dequeue(self):
        if len(self.list) == 0:
            return False
        else:
            return self.list.pop(0)
    def size(self):
        return len(self.list)        
