from Utils.Serializer import Serializer
from Utils.Csv_reader import Csv_reader


class Movie_service:
    def __init__(self, name):
        self._data_reader = Csv_reader("Data/movies.csv")
        self._data_reader.read_from_file()
        self._data = Serializer(self._data_reader.file_content)

    @property
    def data(self):
        return self._data
