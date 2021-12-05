class Movie:
    def __init__(self, id: int, name: str, genere: str):
        self.id = id
        self.name = name
        self.genere = genere

        def __getattr__(self, name):
            try:
                return self.__dict[name]
            except KeyError:
                msg = "'{0}' object has no attribute '{1}'"
                raise AttributeError(msg.format(type(self).__name__, name))
