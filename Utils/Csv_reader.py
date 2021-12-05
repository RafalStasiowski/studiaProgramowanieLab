import csv
from Model.Movie import Movie


class Csv_reader:
    def __init__(self, file_name):
        self._file_name = file_name
        self._file_content = []
        self.read_from_file()

    def read_from_file(self) -> None:
        with open(self._file_name, 'r', encoding="utf8") as read_obj:
            csv_dict_reader = csv.DictReader(read_obj)
            for row in csv_dict_reader:
                self._file_content.append(Movie(row['movieId'], row['title'], row['genres']))


    @property
    def file_content(self) -> list:
        return self._file_content
