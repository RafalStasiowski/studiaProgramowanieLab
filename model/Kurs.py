import model.Pojazd as Pojazd

class Kurs:
    def __init__(self, odcinki: list, pojazd: Pojazd, towar: str, masa_towaru: float, kierowca: str):
        self.__odcinki = odcinki
        self.__pojazd = pojazd
        self.__towar = towar
        self.__masa_towaru = masa_towaru
        self.__kierowca = kierowca

    @property
    def odcinki(self):
        return self.__odcinki

    @odcinki.setter
    def odcinki(self, nowe_odcinki):
        self.__odcinki = nowe_odcinki

    @property
    def pojazd(self):
        return self.__pojazd

    @pojazd.setter
    def pojazd(self, nowy_pojazd):
        self.__pojazd = nowy_pojazd

    @property
    def towar(self):
        return self.__towar

    @towar.setter
    def towar(self, nowy_towar):
        self.__towar = nowy_towar

    @property
    def masa_towaru(self):
        return self.__masa_towaru

    @masa_towaru.setter
    def masa_towaru(self, nowa_masa_towaru):
        self.__masa_towaru = nowa_masa_towaru

    @property
    def kierowca(self):
        return self.__kierowca

    @kierowca.setter
    def kierowca(self, nowy_kierowca):
        self.__kierowca = nowy_kierowca


    def wylicz_sume_kilometrow(self) -> float:
        odleglosc = 0
        for odcinek in self.__odcinki:
            odleglosc = odleglosc + odcinek.dystans
        return odleglosc

    def marka_pojazdu(self) -> str:
        return self.__pojazd.marka

    def __str__(self) -> None:
        return ("Pojazd: {}, towar: {}, masa_towaru: {}, kierowca: {}".format(self.__pojazd,self.__towar, self.__masa_towaru, self.__kierowca))

