from click import echo

from model.student import Student
from model.list_se import ListSE

class ListSEService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListSE()

    def get_all_students(self):
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



