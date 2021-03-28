from DOMAIN.Medicament import Medicament
from DOMAIN.CardClient import CardClient
from DOMAIN.Transaction import Transaction


def test_Medicament():

    m1 = Medicament(1, "Nurofen", "Biofarm", 234.56, "Yes")
    assert m1.id_entity == 1
    assert m1.producer == "Biofarm"
    assert m1.name == "Nurofen"
    assert m1.price == 234.56
    assert m1.recipe == "Yes"


test_Medicament()


def test_CardClient():

    c1 = CardClient(1, "POP", "DAVID", 1045643555327, "15.05.2009", "28.09.2018")
    assert c1.id_entity == 1
    assert c1.date_of_record == "28.09.2018"
    assert c1.birth_date == "15.05.2009"
    assert c1.CNP == 1045643555327
    assert c1.last_name == "POP"
    assert c1.first_name == "DAVID"


test_CardClient()


def test_Transaction():

    t1 = Transaction(11, 1, 1, 6, "25.06.2019", 6.32)
    assert t1.id_entity == 11
    assert t1.id_medicament == 1
    assert t1.id_card_client == 1
    assert t1.nr_pieces == 6
    assert t1.date == "25.06.2019"
    assert t1.hour == 6.32


test_Transaction()
