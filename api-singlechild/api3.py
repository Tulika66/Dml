#run using command FLASK_APP=api3.py flask run --port 5001
#on another terminal, run FLASK_APP=api3.py flask run --port 5002
#run req.py on another terminal



from flask import Flask
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self,a,b):
               
        return a*b

api.add_resource(HelloWorld, '/<int:a>/<int:b>')

if __name__ == '__main__':
    app.run(debug=True)
    