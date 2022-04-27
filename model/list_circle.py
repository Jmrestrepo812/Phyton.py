
from .node import Node
from model.student import Student

class ListCircle:
    def __init__(self):
        self.head= None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

                #posicionados en el ultimo
            temp.next = Node(data)
            temp.next.next=self.head

    def validate_exist(self, id):
        temp=self.head
        while temp != None:
            if temp.data.identification == id:
                return  True
            temp= temp.next
        return False

    def add_to_sart(self, data:Student):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")


            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = Node(data)
            temp.next.next=self.head
            self.head=temp.next

    def listAllStudentsListCircle(self):
        list=[]
        temp = self.head
        while temp.next != self.head:
            list.append(temp.data)

            temp = temp.next

        list.append(temp)
        return list

    def count(self):
        count=0
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
            count+=1

        count=count+1
        return count


