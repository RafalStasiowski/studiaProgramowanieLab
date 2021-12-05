from flask import Flask
from flask_restful import Resource, Api

from Services.Movie_service import Movie_service

app = Flask(__name__)
api = Api(app)


class Main(Resource):
    def get(self):
        return ""


api.add_resource(Main, '/')
api.add_resource(Movie_service, '/movie')

if __name__ == '__main__':
    app.run(debug=True)
