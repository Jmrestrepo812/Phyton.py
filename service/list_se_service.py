from click import echo

from model.student import Student
from model.list_se import ListSE


class ListSEService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListSE()


    def get_all_students(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        return self.students.head

    def add_student(self,data):

        studentCiudad = data['city']
        encontro=0
        for ciudad in self.cities:
            if studentCiudad == ciudad:
                encontro =encontro+1
            else:
                encontro =encontro+0

        if encontro > 0:
            student = Student(data)
            self.students.add(student)
        else:
            raise Exception("La ciudad no es valida")

    def add_student_to_start(self,data):

        studentCiudad = data['city']
        encontro = 0
        for ciudad in self.cities:
            if studentCiudad == ciudad:
                encontro = encontro + 1
            else:
                encontro = encontro + 0

        if encontro > 0:
            student = Student(data)
            self.students.add_to_sart(student)
        else:
            raise Exception("La ciudad no es valida")

    def get_all_students_reverse(self):
        prev = None
        current = self.students.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return prev

    def invert(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.students.invert()
            return {"message": "Se ha invertido la lista"}


    def changeXtremes(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        elif self.students.head.next == None:
            return (self.students)
        else:
            self.students.inverExtremes()
            return {"message": "Se ha invertido la lista"}

    def eliminate_data(self, id):
        self.students.delete_student(id)
        return {"message": "Eliminacion correta de la lista"}


    def eliminate_student_by_position(self, p):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.students.delete_student_by_position(p)
            return {"message": "Eliminacion correta de la lista"}


    def grup_by_gender(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.students.grup_by_gender()
            return {"message": "Se ha organizado la lista por generos"}

    def group_intercalate(self):
        self.students.group_intercalate()
        return {"message": "Lista intercalada por generos la lista"}

    def grup_by_gender_and_age(self):
        self.students.grup_by_gender_and_age()
        return {"message": "Lista intercalada por generos la lista"}

    def insert_by_position(self,p ,data):
        student = Student(data)
        self.students.insert_student_by_position(p, student)
        return {"message": "Inserccion realizada a la lista"}

    def intercalate_by_gender(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.students.group_intercalate()










