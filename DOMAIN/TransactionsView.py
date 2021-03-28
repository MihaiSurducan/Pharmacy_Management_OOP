class TransactionView:

    def __init__(self, transaction, medicament, card_client):

        self.transaction = transaction
        self.medicament = medicament
        self.card_client = card_client

    def __str__(self):
        return '{}. {} -- {}'.format(
            self.transaction.id_entity,
            self.medicament,
            self.card_client
        )

