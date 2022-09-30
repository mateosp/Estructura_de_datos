
from node import Node

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        #self.size = 0

    def notEmpty(self):
        return self.head

    def add(self, data):
        nodo = Node(data)
        if not self.notEmpty():
            self.head = nodo
            self.tail = nodo
        else:
            nodo.next = self.tail
            self.tail = nodo
        

    def print(self):
        current = self.tail
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print()


    def append(self, data):
        node = Node(data)
        if not self.notEmpty():
            self.head = node
        else:
            current = self.tail

            while current.next:
                current = current.next

            current.next = node

        #self.size += 1

   # def size(self):
    #    return str(self.size)

    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val #yield genera valores sobre la marcha, o al aire, para almacenar daros que se pueden usar despues.

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data

            previous = current
            current = current.next

    def search(self, data = int):
        try:
            data = int(input("Digite el numero que desea buscar dentro de la lista de nodos: "))
        except ValueError:
            print("Solo puedes digitar numeros enteros")
        else:
            for node in self.iter():
                if data == node:
                    print (f"Data {data} found")
                    break
                
            if data != node:
                print(f"Data {data} not found, this is the nodes values: ")
               

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0