from model.student import Student
import json

class StudentService:
    students = []
    cities = ['Manizales','Pereira','Chinchiná','Armenia']

    def __init__(self):
        self.students =[]
        #carloaiza = Student({"identification":"75147236","name":"Carlos"})
        #self.students.append(carloaiza)
        self.students.append(Student("363766667", 2, 0, False, "Valentina Hurtado",self.cities[1]))
        self.students.append(Student("233t6363", 1, 0, False, "Kevin Sánchez",self.cities[0]))

    def get_all_students(self):
        return self.students

    def get_percentage_students_by_gender(self,gender):
        count =0
        for student in self.students:
            if student.gender == gender:
                count = count +1
        return count/ len(self.students)

    def get_percentage_students_job_avg_salary(self,gender):
        count=0
        sum_salary=0
        for student in self.students:
            if student.job == True and student.gender == gender:
                count= count +1
                sum_salary = sum_salary + student.salary
        if count > 0 :
            return {"Salario promedio": sum_salary/count,
                "Cantidad": count,
                "% trabajan": count/len(self.students)}
        else:
            return {"Error":"la consulta no generó resultados"}

    def get_students_job_gt_salary(self):
        may_salary_h = None
        may_salary_m = None
        for student in self.students:
            if student.job == True:
                if (student.gender == 1 and may_salary_h == None) or (student.gender == 1 and student.salary > may_salary_h.salary):
                    may_salary_h = student

                if (student.gender == 2 and may_salary_m == None) or (student.gender == 2 and student.salary > may_salary_m.salary):
                    may_salary_m = student

        list_estu=[]
        if may_salary_h != None:
            list_estu.append(may_salary_h)
        if may_salary_m != None:
            list_estu.append(may_salary_m)

        return list_estu

    def get_dict_cities(self):
        dict_cities ={}
        for city in self.cities:
            dict_cities[city]=[0,0]
        return dict_cities

    def get_students_by_city(self):
        dict_cities = self.get_dict_cities()
        for student in self.students:
            if student.job:
                dict_cities[student.city][0]= dict_cities[student.city][0] +1
            else:
                dict_cities[student.city][1] = dict_cities[student.city][1] + 1

        return dict_cities






