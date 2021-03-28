from DOMAIN.CardClient import CardClient
from SERVICE.ServiceError import ServiceError


class CardClientService:

    def __init__(self, repository, transaction_repository):
        self.__repository = repository
        self.__transaction_repository = transaction_repository

    def AddCardClient(self, id_card_client, last_name, first_name, CNP, birth_date, date_of_record):
        cardclient = CardClient(id_card_client, last_name, first_name, CNP, birth_date, date_of_record)
        self.__repository.create(cardclient)
    """
    def __id_card_client_exists_in_transactions(self, id_card_client):
        for transaction in self.__transaction_repository.read():
            if transaction.id_card_client == id_card_client:
                return True
        return False
    """
    def remove_card_client(self, id_card_client):
        if self.__repository.read(id_card_client) is not None:
            self.__repository.delete(id_card_client)
        else:
            raise ServiceError

    def get_all(self):
        return self.__repository.read()
