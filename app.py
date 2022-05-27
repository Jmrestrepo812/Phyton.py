from flask import Flask, jsonify
from controller.student_controller import app_student
from controller.listse_controller import app_list_se
from controller.list_circle import app_list_circle
from controller.listde_controller import app_list_de
from controller.list_circle_de import app_list_circle_de

app = Flask(__name__)
app.register_blueprint(app_student)
app.register_blueprint(app_list_se)
app.register_blueprint(app_list_de)
app.register_blueprint(app_list_circle)
app.register_blueprint(app_list_circle_de)

if __name__ == '__main__':
    app.run()


