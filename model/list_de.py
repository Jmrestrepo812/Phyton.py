from .node_de import Node
from model.student import Student

class ListDe:
    def __init__(self):
        self.head= None
        self.count=0

    def listAllStudentsListDe(self):
        list=[]
        temp = self.head
        while temp != None:
            list.append(temp.data)

            temp = temp.next

        list.append(temp)
        return list


    def add_student_listde(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")

            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = Node(data)
            temp.next.prev=temp

        self.count+=1

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
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")

            temp = Node(data)
            temp.next = self.head
            self.head.prev = temp
            self.head= temp

        self.count +=1

    def invert(self):
        if self.head !=None:
            list_cp=ListDe()
            temp = self.head
            while temp != None:
                list_cp.add_to_sart(temp.data)
                temp = temp.next
            self.head = list_cp.head

    def inverExtremes(self):
       if self.head != None:
           if self.head.next != None:
               list_cp = ListDe()
               cabeza=self.head
               temp= self.head.next
               while temp.next != None:
                   list_cp.add_student_listde(temp.data)
                   temp = temp.next
                   # posicionados en el ultimo
               ultimo=temp
               list_cp.add_student_listde(cabeza.data)
               list_cp.add_to_sart(ultimo.data)
               self.head = list_cp.head

    def delete_student_by_position(self , position):
        if position < 0:
            raise Exception("Estudiante fura del rango")
        elif position == 1:
            self.head=self.head.next
        elif position == self.count:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.prev.next=None

        else:
            posicion=1
            temp = self.head
            while temp.next != None and position != posicion:
                posicion = posicion + 1
                temp = temp.next

            if temp.prev != None:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
        self.count = +1


    def delete_by_id(self, id):

        if self.head.data.identificacion == id:
            if self.head.next == None:
                self.head = None
                return
            elif self.head.next != None:
                self.head = self.head.next
                self.head.prev = None

        temp=self.head
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None

        if temp.data.identification==id:
            temp.prev.next = None
        else:
            temp = self.head
            while temp.next != None:
                if temp.data.identification == id:
                    break;
                temp = temp.next

            if temp.prev != None:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev



    def insert_student_by_position(self, position, data: Student):
        if position < 0 :
            raise Exception("Estudiante fura del rango")
        elif position == 1:
            self.add_to_sart(data)
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")
            node = Node(data)
            temp = self.head
            pres = None
            contador = 1

            while contador < position:
                pres = temp
                temp = temp.next
                contador += 1
            node.next = temp
            temp.prev = node
            pres.next = node
            node.prev = pres
        self.count = +1



    def grup_by_gender(self):
        list_cp = ListDe()
        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                list_cp.add_to_sart(temp.data)
            if temp.data.gender == 2:
                list_cp.add_student_listde(temp.data)
            temp = temp.next
        self.head = list_cp.head
