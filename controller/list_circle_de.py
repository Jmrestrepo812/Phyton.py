from service.list_circle_de import ListCircleDe
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_circle_de = Blueprint("app_list_circle_de",__name__)

list_circle_de_service = ListCircleDe()

@app_list_circle_de.route('/list_circle_de/all')
def get_all_students():

    return Response(status=200,
                    response=json.dumps(list_circle_de_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")


@app_list_circle_de.route('/list_circle_de',methods=['POST'])
def save_student():
    data = request.json
    try:
        list_circle_de_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")


@app_list_circle_de.route('/list_circle_de_add_to_start',methods=['POST'])
def add_student_to_start():

    data = request.json
    try:
        list_circle_de_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")


@app_list_circle_de.route('/list_circle_de_count/all')
def get_count_students():

    return Response(status=200,
                    response=json.dumps(list_circle_de_service.count()
                    ,cls=UtilEncoder),mimetype="application/json")