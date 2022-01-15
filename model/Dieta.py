class Dieta:
    def __init__(self, nazwa: str, cena: float, ile_kcal: float, opis: str):
        self.__nazwa = nazwa
        self.__cena = cena
        self.__ile_kcal = ile_kcal
        self.__opis = opis

    @property
    def nazwa(self):
        return self.__nazwa

    @property
    def cena(self):
        return self.__cena

    @property
    def ile_kcal(self):
        return self.__ile_kcal

    @property
    def opis(self):
        return self.__opis

    def __str__(self):
        return f"Dieta: {self.nazwa}, Cena: {self.cena}, Opis: {self.opis}, Koszt: {self.koszt}"
