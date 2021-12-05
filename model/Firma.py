class Firma:
    def __init__(self,nazwa:str, lokalizacja: str, ilosc_pracownikow: int):
        self.__nazwa = nazwa
        self.__lokalizacja = lokalizacja
        self.__ilosc_pracownikow = ilosc_pracownikow

    @property
    def nazwa(self):
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, nowa_nazwa):
        self.__nazwa = nowa_nazwa

    @property
    def lokalizacja(self):
        return self.__lokalizacja

    @lokalizacja.setter
    def lokalizacja(self, nowa_lokalizacja):
        self.__lokalizacja = nowa_lokalizacja

    @property
    def ilosc_pracownikow(self):
        return self.__ilosc_pracownikow

    @ilosc_pracownikow.setter
    def ilosc_pracownikow(self, nowa_ilosc_pracownikow):
        self.__nowa_ilosc_pracownikow = nowa_ilosc_pracownikow



    def __str__(self) -> None:
        return ("Firma {}, znajdująca się pod adresem {}".format(self.__nazwa, self.__lokalizacja,self.__ilosc_pracownikow))


