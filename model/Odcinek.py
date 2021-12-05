class Odcinek:
    def __init__(self, dystans: float, miejsce_startowe: str, miejsce_docelowe: str, wartosc: float, czy_krajowy: bool):
        self.__dystans = dystans
        self.__miejsce_startowe = miejsce_startowe
        self.__miejsce_docelowe = miejsce_docelowe
        self.__wartosc = wartosc
        self.__czy_krajowy = czy_krajowy

    @property
    def dystans(self):
        return self.__dystans

    @dystans.setter
    def dystans(self, nowy_dystans):
        self.__dystans = nowy_dystans

    @property
    def miejsce_startowe(self):
        return self.__miejsce_startowe

    @miejsce_startowe.setter
    def miejsce_startowe(self, nowe_miejsce_startowe):
        self.__miejsce_startowe = nowe_miejsce_startowe

    @property
    def miejsce_startowe(self):
        return self.__miejsce_docelowe

    @miejsce_startowe.setter
    def miejsce_startowe(self, nowe_miejsce_docelowe):
        self.__miejsce_docelowe = nowe_miejsce_docelowe

    @property
    def wartosc(self):
        return self.__wartosc

    @wartosc.setter
    def wartosc(self, nowa_wartosc):
        self.__wartosc = nowa_wartosc

    @property
    def czy_krajowy(self):
        return self.__czy_krajowy

    @czy_krajowy.setter
    def czy_krajowy(self, nowy_czy_krajowy):
        self.__czy_krajowy = nowy_czy_krajowy


    def __str__(self) -> None:
        return ("Odcinek pomiędzy {} a {}, wartość: {} zł, dystans: {} km".format(self.__miejsce_startowe,self.__miejsce_docelowe, self.__wartosc, self.__dystans))

