from Node import Node

class LinkedList:
  def __init__(self):
    self.Head = None

  #Add new element at the end of the list
  def AddNode(self, data):
      P = Node(data)
      if self.Head == None:
          self.Head = P
          self.ULT = P
      else:
          self.ULT.next = P
          P.prev = self.ULT
          self.ULT = P
        
      self.ULT.next = self.Head
      self.Head.prev = self.ULT

 
  def delete(self, key):
    while(self.Head != None and self.Head.data == key):
      if(self.Head.next == self.Head):
        self.Head = None
      else:
        nodeToDelete = self.Head
        P = self.Head
        while(P.next != self.Head):
          P = P.next
        self.Head = self.Head.next
        P.next = self.Head  
        self.Head.prev = P
        nodeToDelete = None

    P = self.Head        
    if(P != None):
      while(P.next != self.Head):
        if(P.next.data == key):
          nodeToDelete = P.next
          P.next = P.next.next
          P.next.prev = P
          nodeToDelete = None
        else:
          P = P.next


  def PrintList(self):
    P = self.Head
    if(P != None):
      while (True):
        print(P.data, end="<->")
        P = P.next
        if(P == self.Head):
          break
      print()
    else:
      print("None")
      
       