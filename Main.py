from flask import Flask
from flask_restful import Resource, Api

from Services.Movie_service import Movie_service
from Services.Ratings_service import Ratings_service
from Services.Tags_service import Tags_service
from Services.Links_service import Links_service

app = Flask(__name__)
api = Api(app)


class Main(Resource):
    def get(self):
        return ""


api.add_resource(Main, '/')
api.add_resource(Movie_service, '/movies')
#api.add_resource(Ratings_service, '/ratings')
#api.add_resource(Links_service, '/links')
#api.add_resource(Tags_service, '/tags')



if __name__ == '__main__':
    app.run(debug=True)
