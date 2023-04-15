from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

class Division(Resource):
    def get(self, num1, num2):
        num1 = float(num1)
        num2 = float(num2)
        if num2==0.0:
            result = "invalid"
        else:
            result = num1 / num2
        return {'result': result}

api.add_resource(Division, '/<string:num1>/<string:num2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5054,
        host="0.0.0.0"
    )