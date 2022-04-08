from flask import Response, Blueprint, jsonify,json
from service.student_service import StudentService
from util.util_encoder import UtilEncoder

app_student = Blueprint("app_student",__name__)

@app_student.route('/student/all')
def get_all_students():
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_all_students(),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )
    #return jsonify(student_service.get_all_students_dict())

@app_student.route('/student/percentagebygender/<gender>')
def get_percentage_students_by_gender(gender):
    student_service = StudentService()
    return str(student_service.get_percentage_students_by_gender(int(gender)))

@app_student.route('/student/per_students_job_avgsalary/<gender>')
def get_percentage_students_job_avg_salary(gender):
    student_service = StudentService()
    return jsonify(student_service.get_percentage_students_job_avg_salary(int(gender)))

@app_student.route('/student/get_students_job_gt_salary')
def get_students_job_gt_salary():
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_students_job_gt_salary(),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )
@app_student.route('/student/get_students_by_city')
def get_students_by_city():
    student_service = StudentService()
    return jsonify(student_service.get_students_by_city())