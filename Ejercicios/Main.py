from List import List
from LinkedList import LinkedList
from LinkedList2 import LinkedList2

list = List()
list.AddNodo(9)
list.AddNodo(4)
list.AddNodo(3)
list.AddNodo(5)
list.AddNodo(9)
list.AddNodo(7)
list.AddNodo(8)
list.escribirList()

List = LinkedList()
List.AddNode(4)
List.AddNode(6)
List.AddNode(6)
List.AddNode(8)
List.AddNode(10)
List.PrintList()

List.delete(6)
List.PrintList()

MyList = LinkedList2()
MyList.AddNode(1)
MyList.AddNode(2)
MyList.AddNode(3)
MyList.AddNode(4)
MyList.AddNode(5)

MyList.PrintList()
MyList.reverseList()
MyList.PrintList()