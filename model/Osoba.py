class Osoba:
    def __init__(self, imie: str, nazwisko: str, plec: str, wiek: int):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wiek = wiek
        self.__plec = plec

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @property
    def plec(self):
        return self.__plec

    @property
    def wiek(self):
        return self.__wiek

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, {self.plec}, {self.wiek} lat"
