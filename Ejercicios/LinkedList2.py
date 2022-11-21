from Node import Node
class LinkedList2:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def AddNode(self, data):
      P = Node(data)
      if self.head == None:
          self.head = P
          self.ULT = P
      else:
          self.ULT.next = P
          P.prev = self.ULT
          self.ULT = P
        
      self.ULT.next = self.head
      self.head.prev = self.ULT
      
  def reverseList(self):
      
    if(self.head != None):
      prevNode = self.head
      P = self.head
      Nodo = self.head.next
      
      prevNode.next = prevNode
      prevNode.prev = prevNode
      
      while(Nodo != self.head):
        P = Nodo.next

        Nodo.next = prevNode
        prevNode.prev = Nodo
        self.head.next = Nodo
        Nodo.prev = self.head

        prevNode = Nodo
        Nodo = P

      self.head = prevNode 

  #display the content of the list
  def PrintList(self):
    P = self.head
    if(P != None):
      while (True):
        print(P.data, end="<->")
        P = P.next
        if(P == self.head):
          break
      print()
    else:
      print("None")