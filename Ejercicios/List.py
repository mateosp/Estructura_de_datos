from Node import Node

class List:   
    def __init__(self):
        self.Head = None
        self.ULT = None  
        self.contador = 0
        
        
    def AddNodo(self, data):  
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
        
        
    def escribirList(self):
        check = True
        P = self.Head
        while (P != self.Head or check == True):
            print(P.data, end="<->")
            P = P.next
            check = False
        P = self.ULT.next
        print("None")
        
    def __repr__(self):
        respuesta = ""
        P = self.Head
        while(P != None):
            respuesta = respuesta + str(P.data) + "<->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta