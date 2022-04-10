from service.list_se_service import ListSEService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se",__name__)

list_se_service = ListSEService()

@app_list_se.route('/list_se/all')
def get_all_students():

    return Response(status=200,
                    response=json.dumps(list_se_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")

@app_list_se.route('/list_se',methods=['POST'])
def save_student():

    data = request.json
    try:
        list_se_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")


@app_list_se.route('/list_se/all_students_reverse')
def get_all_students_reverse():

    return Response(status=200,
                    response=json.dumps(list_se_service.get_all_students_reverse()
                    ,cls=UtilEncoder),mimetype="application/json")



@app_list_se.route('/list_se_add_to_start',methods=['POST'])
def add_student_to_start():

    data = request.json
    try:
        list_se_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")

@app_list_se.route('/list_se/all_students_invert')
def invert():

    return Response(status=200,
                    response=json.dumps(list_se_service.invert()),mimetype="application/json")

@app_list_se.route('/list_se/ChangeXtremes')
def changeXtremes():

    return Response(status=200,
                    response=json.dumps(list_se_service.changeXtremes()),mimetype="application/json")


@app_list_se.route('/list_se/delete_student/<id>')
def eliminate_data(id):

    return Response(status=200,
                    response=json.dumps(list_se_service.eliminate_data(id)),mimetype="application/json")



@app_list_se.route('/list_se/Order_by_gender')
def grup_by_gender():

    return Response(status=200,
                    response=json.dumps(list_se_service.grup_by_gender()),mimetype="application/json")


@app_list_se.route('/list_se/intercalate_gender')
def group_intercalate():

    return Response(status=200,
                    response=json.dumps(list_se_service.group_intercalate()),mimetype="application/json")