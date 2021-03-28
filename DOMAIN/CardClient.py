from DOMAIN.Entity import Entity


class CardClient(Entity):

    def __init__(self, id_card_client, last_name, first_name, CNP, birth_date, date_of_record):
        """
        Creates a card client
            :param id_card_client: int, the client' card id.
            :param last_name: str, the client' last name.
            :param first_name: str, the client' first name
            :param CNP: int, the client' personal numeric code
            :param birth_date: str, the client' date of record
            :param date_of_record: str,the day of record
        """
        super(CardClient, self).__init__(id_card_client)
        self.__last_name = last_name
        self.__first_name = first_name
        self.__CNP = CNP
        self.__birth_date = birth_date
        self.__date_of_record = date_of_record

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, newLast_name):
        self.__last_name = newLast_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, newFirst_name):
        self.__first_name = newFirst_name

    @property
    def CNP(self):
        return self.__CNP

    @CNP.setter
    def CNP(self, newCNP):
        self.__CNP = newCNP

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, newBirth_date):
        self.__birth_date = newBirth_date

    @property
    def date_of_record(self):
        return self.__date_of_record

    @date_of_record.setter
    def date_of_record(self, newDate_of_record):
        self.__date_of_record = newDate_of_record

    def __str__(self):
        return "CardClient {}, {}, {}, {}, {}, {}".format(self.id_entity,
                                                          self.last_name,
                                                          self.first_name,
                                                          self.CNP,
                                                          self.birth_date,
                                                          self.date_of_record
                                                          )

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_location


