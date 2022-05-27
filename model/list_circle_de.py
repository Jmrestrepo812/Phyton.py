
from .node_cde import Node
from model.student import Student

class ListCircleDe:
    def __init__(self):
        self.count=0
        self.head= None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev=self.head
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            Nodo=Node(data)
            temp.next = Nodo
            Nodo.pre = temp
            Nodo.next = self.head
            self.head.prev=Nodo
        self.count=1

    def validate_exist(self, id):
        temp=self.head
        while temp.next != self.head:
            if temp.data.identification == id:
                return  True
            temp= temp.next

        if temp.data.identification == id:
            return True
        return False

    def add_to_sart(self, data:Student):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev=self.head
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")

            Nodo=Node(data)
            Nodo.next = self.head
            Nodo.pre = self.head.prev
            Nodo.pre.next=Nodo
            self.head.prev=Nodo
            self.head=Nodo
        self.count = 1

    def listAllStudentsListCircle(self):
        list=[]
        temp = self.head
        while temp.next != self.head:
            list.append(temp.data)
            temp = temp.next
        list.append(temp.data)
        return list

    def count(self):
        count=0
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
            count+=1

        count=count+1
        return count