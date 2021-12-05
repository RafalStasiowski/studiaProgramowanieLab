class Pojazd:
    def __init__(self, rodzaj: str, waga: float, maksymalny_udzwig: float, marka: str, numer_rejestracyjny: str):
        self.__rodzaj = rodzaj
        self.__waga = waga
        self.__maksymalny_udzwig = maksymalny_udzwig
        self.__marka = marka
        self.__numer_rejestracyjny = numer_rejestracyjny

    @property
    def rodzaj(self):
        return self.__rodzaj

    @rodzaj.setter
    def nazwa(self, nowy_rodzaj):
        self.__rodzaj = nowy_rodzaj

    @property
    def waga(self):
        return self.__waga

    @waga.setter
    def waga(self, nowa_waga):
        self.__waga = nowa_waga

    @property
    def maksymalny_udzwig(self):
        return self.__maksymalny_udzwig

    @maksymalny_udzwig.setter
    def maksymalny_udzwig(self, nowy_maksymalny_udzwig):
        self.__maksymalny_udzwig = nowy_maksymalny_udzwig

    @property
    def marka(self):
        return self.__marka

    @marka.setter
    def marka(self, nowa_marka):
        self.__maksymalny_udzwig = nowa_marka

    @property
    def numer_rejestracyjny(self):
        return self.__numer_rejestracyjny

    @numer_rejestracyjny.setter
    def numer_rejestracyjny(self, nowy_numer_rejestracyjny):
        self.__numer_rejestracyjny = nowy_numer_rejestracyjny


    def __str__(self) -> None:
        return ("Pojazd marki {}, o numerze rejestracyjnym: {}. Max udźwig: {}, waga: {}".format(self.__marka,self.__numer_rejestracyjny, self.__maksymalny_udzwig, self.__waga))

