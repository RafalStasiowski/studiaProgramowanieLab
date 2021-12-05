class Serializer:
    def __init__(self, to_serialize: list):
        self._to_serialize = to_serialize
        self._serialized = []
        self.serialize()

    def serialize(self) -> None:

        for item in self._to_serialize:
            self._serialized.append(item.__dict__)

    @property
    def serialized(self):
        return self._serialized
