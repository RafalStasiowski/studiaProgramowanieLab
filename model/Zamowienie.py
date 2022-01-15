from model.Pacjent import Pacjent
from model.Dietetyk import Dietetyk


class Zamowienie:
    def __init__(self):
        self.__opis = None

    @property
    def diety(self):
        return self.__diety

    @diety.setter
    def diety(self, diety):
        self.__diety = diety

    @property
    def pacjent(self):
        return self.__pacjent

    @pacjent.setter
    def pacjent(self, pacjent):
        self.__pacjent = pacjent

    @property
    def dietetyk(self):
        return self.__dietetyk

    @dietetyk.setter
    def dietetyk(self, dietetyk):
        self.__dietetyk = dietetyk

    @property
    def opis(self):
        return self.__opis

    @opis.setter
    def opis(self, opis):
        self.__opis = opis

    def suma(self) -> float:
        wartosc_zamowienia = 0
        for dieta in self.__diety:
            wartosc_zamowienia += dieta.cena
        return round(wartosc_zamowienia, 2)

    def suma_kalorii(self) -> float:
        ile_kcal = 0
        for dieta in self.__diety:
            ile_kcal += dieta.ile_kcal
        return ile_kcal

    def __str__(self):
        return f"{self.opis} - Pacjent: {self.pacjent}, Dietetyk: {self.dietetyk}"
