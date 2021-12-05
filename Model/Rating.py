class Movie:
    def __init__(self, id: int, movie_id: int, rating: float, timestamp: int):
        self.id = id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

        def __getattr__(self, name):
            try:
                return self.__dict[name]
            except KeyError:
                msg = "'{0}' object has no attribute '{1}'"
                raise AttributeError(msg.format(type(self).__name__, name))
