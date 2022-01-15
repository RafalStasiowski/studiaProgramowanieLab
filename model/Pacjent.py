from model.Osoba import Osoba


class Pacjent(Osoba):
    def __init__(self, imie: str, nazwisko: str, plec: str, wiek: int):
        super().__init__(imie, nazwisko, wiek, plec)

    def __str__(self):
        return super(Pacjent, self).__str__()
