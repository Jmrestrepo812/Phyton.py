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

            new_node=Node(data)
            temp.next = new_node
            new_node.prev=temp

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
            self.head.prev=None
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

            if temp.next != None:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
        self.count-=1


    def delete_by_id(self, id):
        if self.head.data.identification == id:
            if self.head.next == None:
                self.head = None
                return
            elif self.head.next != None:
                self.head = self.head.next
                self.head.prev = None
        else:
            ##eliminar intermedio
            temp = self.head
            while temp.next != None :
                if temp.data.identification == id:
                    break
                temp = temp.next
            if temp.next != None:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            else:
                ##eliminar dato final
                if temp.data.identification == id:
                    temp.prev.next = None
        self.count = -1



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

    def group_intercalate(self):
        contadoM=0
        contadoW=0
        list_cp_man = ListDe()
        list_cp_women = ListDe()
        list_cp_bought_genders = ListDe()
        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                list_cp_man.add_student_listde(temp.data)
                contadoM=contadoM+1
            if temp.data.gender == 2:
                contadoW=contadoW+1
                list_cp_women.add_student_listde(temp.data)
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
                    list_cp_bought_genders.add_student_listde(tempW.data)
                    tempW = tempW.next

            if tempM != None:
                if tempM.data != None:
                    list_cp_bought_genders.add_student_listde(tempM.data)
                    tempM = tempM.next
            MayorLongitud = MayorLongitud-1
        self.head = list_cp_bought_genders.head

    def group_by_gender_and_age(self):
        ageMens = []
        ageWomens = []
        list_cp_man = ListDe()
        list_cp_women = ListDe()

        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                list_cp_man.add_student_listde(temp.data)
                ageMens.append(temp.data.age)
            if temp.data.gender == 2:
                list_cp_women.add_student_listde(temp.data)
                ageWomens.append(temp.data.age)
            temp = temp.next
        print(ageMens)
        print(ageWomens)
        ageMens.sort()
        ageWomens.sort()

        list_cp_mans_sorted = ListDe()
        list_cp_womens_sorted = ListDe()

        for edadMens in ageMens:
            temp = list_cp_man.head
            while temp != None:
                if edadMens == temp.data.age:
                    list_cp_mans_sorted.add_student_listde(temp.data)
                temp = temp.next

        for edadWomens in ageWomens:
            temp = list_cp_women.head
            while temp != None:
                if edadWomens == temp.data.age:
                    list_cp_womens_sorted.add_to_sart(temp.data)
                temp = temp.next

        list_bought_genders = ListDe()
        tempWomensSorted = list_cp_womens_sorted.head
        while tempWomensSorted != None:
            list_bought_genders.add_student_listde(tempWomensSorted.data)
            tempWomensSorted = tempWomensSorted.next

        tempMensSorted = list_cp_mans_sorted.head
        while tempMensSorted != None:
            list_bought_genders.add_student_listde(tempMensSorted.data)
            tempMensSorted = tempMensSorted.next

        self.head = list_bought_genders.head
