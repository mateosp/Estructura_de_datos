
from SinglyLinkedList import SinglyLinkedList, Node
import random, collections

if __name__ == "__main__":
    nodos = SinglyLinkedList()
    nodos2 = SinglyLinkedList()
    lista1 = []
    lista2 = []
    for x in range (1, 6): 
        temp = random.randint(1, 1)
        nodos.add(temp)
        nodos.append(temp)
        lista1.append(temp) 
    nodos.search()
    nodos.print() 
    #print(lista1)
    
    for x in range (1, 6): 
        temp2 = random.randint(1, 1)
        nodos2.add(temp2)
        nodos2.append(temp2)
        lista2.append(temp2)
    nodos2.search()
    nodos2.print()
    #print(lista2)
       
    if collections.Counter(lista1) == collections.Counter(lista2):
        print("La lista de nodos son semejantes")
    else:
        print("No son semejantes")
    
    


