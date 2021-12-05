import model.Firma as Firma

class FirmaTransportowa(Firma):
    def __init__(self,nazwa:str, lokalizacja: str, ilosc_pracownikow: int, pojazdy: list, kursy: list, kierowcy: list):
        super.__init__(nazwa,lokalizacja,ilosc_pracownikow)
        self.__pojazdy = pojazdy
        self.__kursy = kursy
        self.__kierowcy = kierowcy

    @property
    def pojazdy(self):
        return self.__pojazdy

    @pojazdy.setter
    def pojazdy(self, nowe_pojazdy):
        self.__pojazdy = nowepojazdy

    def __str__(self) -> None:
        super.__str__()
        return (" Pojazdy: {}, kursy: {}, kierowcy: {}, kierowca: {}".format(self.__pojazdy,self.__kursy, self.__kierowcy))
