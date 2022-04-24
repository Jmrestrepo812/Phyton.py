from service.list_circle import ListCircle
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_circle = Blueprint("app_list_se",__name__)

list_circle_service = ListCircle()

@app_list_circle.route('/list_se',methods=['POST'])
def save_student():
    data = request.json
    try:
        list_circle_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str (e)}),
                        mimetype="application/json")
