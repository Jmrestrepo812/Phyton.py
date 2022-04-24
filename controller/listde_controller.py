from service.list_de_service import ListDEService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_de = Blueprint("app_list_de",__name__)

list_de_service = ListDEService()

@app_list_de.route('/list_de/all')
def get_all_students():

    return Response(status=200,
                    response=json.dumps(list_de_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")


@app_list_de.route('/list_de',methods=['POST'])
def save_student():

    data = request.json
    try:
        list_de_service.add_student_listde(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")



@app_list_de.route('/list_de_add_to_start',methods=['POST'])
def add_student_to_start():

    data = request.json
    try:
        list_de_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")


@app_list_de.route('/list_de/all_students_invert')
def invert():

    return Response(status=200,
                    response=json.dumps(list_de_service.invert()
                    ,cls=UtilEncoder),mimetype="application/json")

@app_list_de.route('/list_de/ChangeXtremes')
def changeXtremes():

    return Response(status=200,
                    response=json.dumps(list_de_service.changeXtremes()),mimetype="application/json")

@app_list_de.route('/list_de/delete_student_by_position/<position>')
def eliminate_data(position):
    try:
        list_de_service.eliminate_data_by_position(int(position))
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")



@app_list_de.route('/list_de/insert_student_by_position/<position>',methods=['POST'])
def insert_student_by_position(position):

    data = request.json
    try:
        list_de_service.insert_student_by_position(int(position),data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")

@app_list_de.route('/list_de/delete_student_by_id/<id>')
def eliminate_student_by_id(id):

    return Response(status=200,
                    response=json.dumps(list_de_service.eliminate_data_by_id(int(id))), mimetype="application/json")

@app_list_de.route('/list_de/group_by_gender')
def group_intercalate():

    return Response(status=200,
                    response=json.dumps(list_de_service.group_intercalate()),mimetype="application/json")