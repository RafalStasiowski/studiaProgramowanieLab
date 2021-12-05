from Utils.Serializer import Serializer
from Utils.Csv_reader import Csv_reader
from flask_restful import Resource


class Ratings_service(Resource):

    def get(self):
        data_reader = Csv_reader("Data/ratings.csv")
        serializer = Serializer(data_reader.file_content)
        return serializer.serialized
