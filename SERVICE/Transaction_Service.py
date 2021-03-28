from DOMAIN.Transaction import Transaction
from DOMAIN.TransactionsView import TransactionView
from SERVICE.ServiceError import ServiceError


class TransactionService:

    def __init__(self, transaction_repository, medicament_repository, card_client_repository):
        self.__transaction_repository = transaction_repository
        self.__medicament_repository = medicament_repository
        self.__card_client_repository = card_client_repository

    def AddTransaction(self, id_transaction, id_medicament, id_card_client, nr_pieces, date, hour):

        if self.__medicament_repository.read(id_medicament) is None:
            raise ValueError('There is no medicine with the given id: ' + id_medicament)
        if self.__card_client_repository.read(id_card_client) is None:
            raise ValueError('There is no card client with the given id : ' + id_card_client)

        transaction = Transaction(id_transaction, id_medicament, id_card_client, nr_pieces, date, hour)
        self.__transaction_repository.create(transaction)

    def remove_transaction(self, id_transaction):

        if self.__transaction_repository.read(id_transaction) is not None:
            self.__transaction_repository.delete(id_transaction)
        else:
            raise ServiceError()

    def get_all(self):
        return self.__transaction_repository.read()
