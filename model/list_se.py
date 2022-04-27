from werkzeug.routing import Map

from .node import Node
from model.student import Student
class ListSE:
    def __init__(self):
        self.head= None
        self.count = 0

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
        self.count +=1

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
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")
            temp=Node(data)
            temp.next = self.head
            self.head = temp

        self.count+=1

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

    def delete_student_by_position(self,p):
        posicion = 1
        if p == 1 and self.head.data != None:
            self.head = self.head.next

        temp = self.head
        while temp.next != None:
            posicion=posicion+1
            if temp.next.data !=  None and p == posicion:
                temp.next = temp.next.next
                break;
            temp = temp.next

    def insert_student_by_position(self,position ,data:Student):
        if position > 0 :
            if position == 1:
                self.add_to_sart(data)

            else:
                temp = self.head
                count = 1
                while temp != None:
                    if count == position - 1:
                        new_node = Node(data)
                        if self.validate_exist(data.identification):
                            raise Exception("Ya existe un estudiante con esa identificacion")
                        new_node.next = temp.next
                        temp.next = new_node
                        self.count = +1
                        break
                    temp = temp.next
                    count = +1

            self.count = +1
        else:
            raise Exception("La posición no es válida")



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
                list_cp_man.add(temp.data)
                contadoM=contadoM+1
            if temp.data.gender == 2:
                contadoW=contadoW+1
                list_cp_women.add(temp.data)
            temp = temp.next

        if contadoM>contadoW:
            MayorLongitud=contadoM
        else:
            MayorLongitud = contadoW

        tempM =list_cp_man.head
        tempW = list_cp_women.head

        while MayorLongitud > 0:
        ##for x in range(1, MayorLongitud):

            if tempW != None:
                if tempW.data != None:
                    list_cp_bought_genders.add(tempW.data)
                    tempW = tempW.next

            if tempM != None:
                if tempM.data != None:
                    list_cp_bought_genders.add(tempM.data)
                    tempM = tempM.next
            MayorLongitud = MayorLongitud-1
        self.head = list_cp_bought_genders.head


    def grup_by_gender_and_age(self):
        ageMens=[]
        ageWomens=[]
        list_cp_man = ListSE()
        list_cp_women = ListSE()
        list_cp_bought_genders = ListSE()
        temp= self.head

        while temp != None:
            if temp.data.gender == 1:
                list_cp_man.add(temp.data)
                ageMens.append(temp.data.age)
            if temp.data.gender == 2:
                list_cp_women.add(temp.data)
                ageWomens.append(temp.data.age)
            temp = temp.next
        print(ageMens)
        print(ageWomens)
        #sortedListMens=\
        ageMens.sort()
        #sortedListWomens=\
        ageWomens.sort()

        list_cp_mans_sorted = ListSE()
        list_cp_womens_sorted = ListSE()

        for edadMens in ageMens:
            temp=list_cp_man.head
            while temp.next != None:
                if edadMens == temp.data.age:
                    list_cp_mans_sorted.add(temp.data)
                temp = temp.next

        for edadWomens in ageWomens:
            temp=list_cp_women.head
            while temp.next != None:
                if edadWomens == temp.data.age:
                    list_cp_womens_sorted.add(temp.data)
                temp = temp.next



        tempwomensSorted = list_cp_womens_sorted.head
        while tempwomensSorted != None:
            list_cp_bought_genders.add(tempwomensSorted.data)
            tempwomensSorted= tempwomensSorted.next

        tempMensSorted = list_cp_mans_sorted.head
        while tempMensSorted != None:
            list_cp_bought_genders.add(tempMensSorted.data)
            tempMensSorted = tempMensSorted.next

        self.head=list_cp_bought_genders.head





