from DOMAIN.Entity import Entity


class Transaction(Entity):

    def __init__(self, id_transaction, id_medicament, id_card_client, nr_pieces, date, hour):
        """
        Creates a card client
            :param id_transaction: int, the transaction id
            :param id_medicament: int, the medicament id
            :param id_card_client: int, the card client id
            :param nr_pieces: int, the number of pieces
            :param date: str, the date of transaction
            :param hour: flaot, the hour of transaction
        """
        super(Transaction, self).__init__(id_transaction)
        self.__id_medicament = id_medicament
        self.__id_card_client = id_card_client
        self.__nr_pieces = nr_pieces
        self.__date = date
        self.__hour = hour

    @property
    def id_medicament(self):
        return self.__id_medicament

    @id_medicament.setter
    def id_medicament(self, newId_medicament):
        self.__id_medicament = newId_medicament

    @property
    def id_card_client(self):
        return self.__id_card_client

    @id_card_client.setter
    def id_card_client(self, newId_card_client):
        self.__id_card_client = newId_card_client

    @property
    def nr_pieces(self):
        return self.__nr_pieces

    @nr_pieces.setter
    def nr_pieces(self, newNr_pieces):
        self.__nr_pieces = newNr_pieces

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, newDate):
        self.__date = newDate

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, newHour):
        self.__hour = newHour

    def __str__(self):
        return 'ID Transaction:{}  ID Medicament:{}  ID Card:{}  Number of Pieces:{}  Date:{}  Hour:{}'.format(self.id_entity, self.id_medicament, self.id_card_client,
                                                                                                               self.nr_pieces, self.date, self.hour)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity
