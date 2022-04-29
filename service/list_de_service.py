from click import echo

from model.student import Student
from model.list_de import ListDe


class ListDEService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListDe()

    def get_all_students(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        return self.students.listAllStudentsListDe()

    def add_student_listde(self, data):

        studentCiudad = data['city']
        encontro = 0
        for ciudad in self.cities:
            if studentCiudad == ciudad:
                encontro = encontro + 1
            else:
                encontro = encontro + 0

        if encontro > 0:
            student = Student(data)
            self.students.add_student_listde(student)
        else:
            raise Exception("La ciudad no es valida")

    def add_student_to_start(self,data):

        studentCiudad = data['city']
        encontro=0
        for ciudad in self.cities:
            if studentCiudad == ciudad:
                encontro =encontro+1
            else:
                encontro =encontro+0

        if encontro > 0:
            student = Student(data)
            self.students.add_to_sart(student)
        else:
            raise Exception("La ciudad no es valida")

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

    def eliminate_data_by_position(self, p):
        self.students.delete_student_by_position(p)
        return {"message": "Eliminacion correta de la lista"}

    def insert_student_by_position(self , p, data):
        student = Student(data)
        self.students.insert_student_by_position(p, student)
        return {"message": "Estudiante insertado a la lista"}


    def eliminate_data_by_id(self, id):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.students.delete_by_id(id)
            return {"message": "estudiante eliminado"}

    def group_intercalate(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.students.grup_by_gender()
            return {"message": "Lista intercalada por generos la lista"}


    def group_intercalate_by_gender(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.students.group_intercalate()
            return {"message": "Lista intercalada por generos individualmente la lista"}

    def group_intercalate_by_gender_and_age(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            self.students.group_by_gender_and_age()
            return {"message": "Lista intercalada por generos individualmente la lista"}