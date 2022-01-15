from model.Osoba import Osoba


class Dietetyk(Osoba):
    def __init__(self, imie: str, nazwisko: str, plec: str, wiek: int, koszt_za_godzine: float):
        super().__init__(imie, nazwisko, plec, wiek)
        self.__koszt_za_godzine = koszt_za_godzine

    @property
    def koszt_za_godzine(self):
        return self.__koszt_za_godzine

    def __str__(self):
        return super(Dietetyk, self).__str__() + f" koszt za godzine: {self.koszt_za_godzine}"
