
from model.student import Student
from model.list_circle import ListCircle

class ListSEService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListCircle()


    def get_all_students(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        return self.students.listAllStudentsListCircle()

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

    def count(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        return self.students.count()