from flask import Flask, jsonify, send_from_directory
from flask_restful import Resource, Api
from flask_cors import CORS
from crawler import crawler_userinfo
# from sqlalchemy import create_engine
# from json import dumps


app = Flask(__name__,
            static_url_path='',
            static_folder='./static')
api = Api(app)
CORS(app)


# db_connect = create_engine('sqlite:///chinook.db')
# conn = db_connect.connect() #kết nối với cơ sở dữ liệu


class live_video(Resource):
    def get(self, comment_id):
        user_info = crawler_userinfo(comment_id)
        print('user info', user_info)
        return {'user': user_info}


# class Tracks(Resource):
#     def get(self):
#         query = conn.execute("select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# class Employees_Name(Resource):
#     def get(self, employee_id):
#         query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)


api.add_resource(live_video, '/live_video/<comment_id>')  # Route_1

# api.add_resource(Tracks, '/tracks') # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


@app.route('/policy')
def policy(path):
    return send_from_directory('static')
