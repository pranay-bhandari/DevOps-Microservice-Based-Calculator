from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_restful import Resource, Api

app = Flask(_name_)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

class Exponent(Resource):
    def get(self, num1, num2):
        result = float(num1)**float(num2)
        return {'result': result}

api.add_resource(Exponent, '/<string:num1>/<string:num2>')

if _name_ == '_main_':
    app.run(
        debug=True,
        port=5057,
        host="0.0.0.0"
    )