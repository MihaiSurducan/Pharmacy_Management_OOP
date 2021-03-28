from REPOSITORY.GenericFileRepository import GenericFileRepository
from DOMAIN.Medicament_Validator import MedicamentValidator
from SERVICE.Medicament_Service import MedicamentService
from SERVICE.CardClient_Service import CardClientService
from SERVICE.Transaction_Service import TransactionService
from UI.console import Console


medicament_repository = GenericFileRepository('medicament.pkl')
card_client_repository = GenericFileRepository('cardclient.pkl')
transaction_repository = GenericFileRepository('transaction.pkl')


medicament_validator = MedicamentValidator()


medicament_service = MedicamentService(medicament_repository, transaction_repository, medicament_validator)
card_client_service = CardClientService(card_client_repository, transaction_repository)
transaction_service = TransactionService(transaction_repository, medicament_repository, card_client_repository)

console = Console(medicament_service, card_client_service, transaction_service)
console.run_console()
