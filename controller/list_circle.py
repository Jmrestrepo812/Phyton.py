from service.list_circle import ListCircle
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_circle = Blueprint("app_list_se",__name__)

list_circle_service = ListCircle()

@app_list_circle.route('/list_circle/all')
def get_all_students():

    return Response(status=200,
                    response=json.dumps(list_circle_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")


@app_list_circle.route('/list_circle',methods=['POST'])
def save_student():
    data = request.json
    try:
        list_circle_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")


@app_list_circle.route('/list_circle_add_to_start',methods=['POST'])
def add_student_to_start():

    data = request.json
    try:
        list_circle_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")


@app_list_circle.route('/list_circle_count/all')
def get_all_students():

    return Response(status=200,
                    response=json.dumps(list_circle_service.count()
                    ,cls=UtilEncoder),mimetype="application/json")


