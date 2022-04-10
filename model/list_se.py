from werkzeug.routing import Map

from .node import Node
from model.student import Student
class ListSE:
    def __init__(self):
        self.head= None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")


            temp = self.head
            while temp.next != None:
                temp = temp.next

                #posicionados en el ultimo
            temp.next = Node(data)

    def validate_exist(self, id):
        temp=self.head
        while temp != None:
            if temp.data.identification == id:
                return  True
            temp= temp.next
        return False

    def add_to_sart(self, data:Student):
        if self.head == None:
            self.head= Node(data)
        else:
            temp=Node(data)
            temp.next = self.head
            self.head = temp

    def invert(self):
        if self.head !=None:
            list_cp=ListSE()
            temp = self.head
            while temp != None:
                list_cp.add_to_sart(temp.data)
                temp = temp.next
            self.head = list_cp.head

    def inverExtremes(self):
       if self.head != None:
           if self.head.next != None:
               list_cp = ListSE()
               cabeza=self.head
               temp= self.head.next
               while temp.next != None:
                   list_cp.add(temp.data)
                   temp = temp.next
                   # posicionados en el ultimo
               ultimo=temp
               list_cp.add(cabeza.data)
               list_cp.add_to_sart(ultimo.data)
               self.head = list_cp.head

    def delete_student(self,id):
        if id == self.head.data.identification:
            self.head=self.head.next
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.data.identification == id:
                    temp.next=temp.next.next
                    break;
                temp=temp.next



    def grup_by_gender(self):
        list_cp = ListSE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                list_cp.add_to_sart(temp.data)
            if temp.data.gender == 2:
                list_cp.add(temp.data)
            temp = temp.next
        self.head = list_cp.head

    def group_intercalate(self):
        contadoM=0
        contadoW=0
        list_cp_man = ListSE()
        list_cp_women = ListSE()
        list_cp_bought_genders = ListSE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                list_cp_man.add_to_sart(temp.data)
                contadoM=contadoM+1
            if temp.data.gender == 2:
                contadoW=contadoW+1
                list_cp_women.add(temp.data)
            temp = temp.next

        if contadoM>contadoW:
            MayorLongitud=contadoM
        else:
            MayorLongitud = contadoW

        tempM=list_cp_man.head
        tempW = list_cp_women.head

        for x in range(1, MayorLongitud):
            if tempM.data!= None:
                list_cp_bought_genders.add(tempM.data)
            if tempW.data != None:
                list_cp_bought_genders.add(tempW.data)
            tempM = tempM.next
            tempW = tempW.next
        self.head = list_cp_bought_genders.head





