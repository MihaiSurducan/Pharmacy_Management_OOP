from REPOSITORY.Repository_Error import RepositoryError
from SERVICE.ServiceError import ServiceError

class Console:

    def __init__(self, medicament_service, card_client_service, transaction_service):
        self.__medicament_service = medicament_service
        self.__card_client_service = card_client_service
        self.__transaction_service = transaction_service

    def __show_menu(self):
        print('1. Medicine')
        print('2. Card Client')
        print('3. Transaction')
        print('x. Exit')

    def run_console(self):

        while True:
            self.__show_menu()
            op = input('Option: ')
            if op == '1':
                self.__show_medicament()
            elif op == '2':
                self.__show_card_client()
            elif op == '3':
                self.__show_transaction()
            elif op == 'x':
                break
            else:
                print('Invalid command!')

    def __show_medicament(self):

        while True:
            self.__show_menu_medicament()
            op = input('Option: ')
            if op == '1':
                self.__handle_medicament_add()
            elif op == '2':
                self.__handle_medicament_remove()
            elif op == '3':
                self.__handle_medicament_increase()
            elif op == '4':
                self.__show_list(self.__medicament_service.get_sorted_by_name())
            elif op == '5':
                self.__handle_populate_medicament()
            elif op == 'a':
                self.__show_list(self.__medicament_service.get_all())
            elif op == 'b':
                break
            else:
                print('Invalid Command!')

    def __show_menu_medicament(self):
        print('--- Medicine')
        print('1. Add')
        print('2. Remove')
        print('3. Increase the price from a specific value')
        print('4. Sort by name')
        print('5. Populate random')
        print('a. Print All')
        print('b. Back')

    def __handle_medicament_increase(self):
        try:
            increase_price = float(input('Give the value from where you want to increase the prices : '))
            self.__medicament_service.raisePriceByOne(increase_price)
        except Exception as e:
            print(e)

    def __handle_medicament_add(self):
        try:
            id_medicament = input('ID : ')
            while type(id_medicament) is not int:
                try:
                    id_medicament = int(id_medicament)
                except ValueError:
                    print("The ID must be a natural number")
                    id_medicament = input("ID : ")
            name = input('NAME : ')
            while name == "":
                try:
                    name = input('Name : ')
                except Exception as e:
                    print(e)
            producer = input('The name of the PRODUCER : ')
            price = input('PRICE : ')
            while type(price) is not float:
                try:
                    price = float(price)
                except ValueError:
                    print("The Price must be a rational number")
                    price = input("PRICE : ")
            recipe = input('RECIPE :  (Yes or No)')
            self.__medicament_service.AddMedicament(
                id_medicament,
                name,
                producer,
                price,
                recipe
            )
            print('The Medicine has been successfully added!')
        except RepositoryError as re:
            print('Eroare:', re)

    def __handle_populate_medicament(self):
        n = input("How many new medicaments would you like to add random: ")
        while type(n) is not int:
            try:
                n = int(n)
            except ValueError:
                print("Please give a natural number for how many new medicaments would you like to add random")
                n = input("How many new medicaments would you like to add random : ")
        self.__medicament_service.populate(n)

    def __show_list(self, objects):
        for object in objects:
            print(object)

    def __show_card_client(self):
        while True:
            self.__show_menu_card_client()
            op = input('Option: ')
            if op == '1':
                self.__handle_card_client_add()
            elif op == '2':
                self.__handle_cardclient_remove()
            elif op == 'a':
                self.__show_list(self.__card_client_service.get_all())
            elif op == 'b':
                break
            else:
                print('Invalid command!')

    def __show_menu_card_client(self):
        print('--- Card Client')
        print('1. Add')
        print('2. Remove')
        print('a. Print')
        print('b. Back')

    def __handle_card_client_add(self):
        try:
            id_card_client = input('Card Client ID : ')
            while type(id_card_client) is not int:
                try:
                    id_card_client = int(id_card_client)
                except ValueError:
                    print("The Card Client ID must be a natural number")
                    id_card_client = input("ID : ")
            last_name = input('The LAST NAME of the client : ')
            first_name = input('THE FIRST NAME of the client : ')
            CNP = input('The client personal numeric code : ')
            birth_date = input('The client date of birth: ')
            date_of_record = input('Date of record: ')
            self.__card_client_service.AddCardClient(
                id_card_client,
                last_name,
                first_name,
                CNP,
                birth_date,
                date_of_record
            )
            print('Card Client has been successfully added!')
        except RepositoryError as re:
            print('Eroare:', re)

    def __show_transaction(self):
        while True:
            self.__show_menu_transaction()
            op = input('Option: ')
            if op == '1':
                self.__handle_transaction_add()
            elif op == '2':
                self.__handle_transaction_remove()
            elif op == '3':
                self.__handle_transaction_show()
            elif op == 'a':
                self.__show_list(self.__transaction_service.get_all())
            elif op == 'b':
                break
            else:
                print('Invalid command!')

    def __show_menu_transaction(self):
        print('--- Transaction')
        print('1. Add')
        print('2. Remove transactions in an interval')
        print('3. Show transactions in an interval')
        print('a. Print')
        print('b. Back')

    def __handle_transaction_add(self):
        try:
            id_transaction = input('Transaction ID : ')
            while type(id_transaction) is not int:
                try:
                    id_transaction = int(id_transaction)
                except ValueError:
                    print("The Transaction ID must be a natural number")
                    id_transaction = input("Transaction ID : ")
            id_medicament = input('Medicine ID : ')
            while type(id_medicament) is not int:
                try:
                    id_medicament = int(id_medicament)
                except ValueError:
                    print("The Medicine ID must be a natural number")
                    id_medicament = input("Medicine ID : ")
            id_card_client = input('Card Client ID : ')
            while type(id_card_client) is not int:
                try:
                    id_card_client = int(id_card_client)
                except ValueError:
                    print("The Card Client ID must be a natural number")
                    id_card_client = input("Card Client ID : ")
            nr_pieces = input('Number of pieces : ')
            while type(nr_pieces) is not int:
                try:
                    nr_pieces = int(nr_pieces)
                except ValueError:
                    print("The number of pieces must be a natural number")
                    nr_pieces = input("Number of pieces : ")
            date = input('DATE : ')
            hour = input('HOUR: ')
            self.__transaction_service.AddTransaction(
                id_transaction,
                id_medicament,
                id_card_client,
                nr_pieces,
                date,
                hour
            )
            print('Transaction has been completely added!')
        except ValueError as ve:
            print('Error:')
            for error in ve.args[0]:
                print(error)

    def __handle_medicament_remove(self):
        """
        Removes a medicine in every transaction that it shows up
        """
        try:
            id_medicament = input('Give the ID that you would like to remove: ')
            while type(id_medicament) is not int:
                try:
                    id_medicament = int(id_medicament)
                except ValueError:
                    print("The ID must be a natural number")
                    id_medicament = input("Give the ID that you would like to remove : ")
            self.__medicament_service.remove_medicament(id_medicament)
            print("The medicine with the given ID has been successfully removed")
            for transaction in self.__transaction_service.get_all():
                if transaction.id_medicament == id_medicament:
                    self.__transaction_service.remove_transaction(transaction.id_entity)
                    print("The transaction has been succesfully removed!")
        except ValueError:
            print("The ID is wrong")
        except ServiceError:
            print("There is no medicine with the given id!")

    def __handle_transaction_remove(self):
        """
        Removes transactions between two given dates
        """
        date1 = input("Introduce the begin of the interval: ")
        date2 = input("Introduce the end of the interval: ")
        process_date1 = date1.split(".")
        process_date2 = date2.split(".")
        for transaction in self.__transaction_service.get_all():
            process_date3 = transaction.date.split(".")
            if process_date1[2] < process_date3[2] < process_date2[2]:
                self.__transaction_service.remove_transaction(transaction.id_entity)
            elif process_date1[2] == process_date3[2] or process_date2[2] == process_date3[2]:
                if process_date1[1] < process_date3[1] < process_date2[1]:
                    self.__transaction_service.remove_transaction(transaction.id_entity)
                elif process_date1[1] == process_date3[1] or process_date2[1] == process_date3[1]:
                    if process_date1[0] < process_date3[0] < process_date2[0]:
                        self.__transaction_service.remove_transaction(transaction.id_entity)
                    elif process_date1[0] == process_date3[0] or process_date2[0] == process_date3[0]:
                        self.__transaction_service.remove_transaction(transaction.id_entity)
                    else:
                        break
                else:
                    break
            else:
                break

    def __handle_transaction_show(self):
        """
        Shows transactions between two given dates
        """
        date1 = input("Introduce the begin of the interval: ")
        date2 = input("Introduce the end of the interval: ")
        process_date1 = date1.split(".")
        process_date2 = date2.split(".")
        for transaction in self.__transaction_service.get_all():
            process_date3 = transaction.date.split(".")
            if process_date1[2] < process_date3[2] < process_date2[2]:
                print(transaction)
            elif process_date1[2] == process_date3[2] or process_date2[2] == process_date3[2]:
                if process_date1[1] < process_date3[1] < process_date2[1]:
                    print(transaction)
                elif process_date1[1] == process_date3[1] or process_date2[1] == process_date3[1]:
                    if process_date1[0] < process_date3[0] < process_date2[0]:
                        print(transaction)
                    elif process_date1[0] == process_date3[0] or process_date2[0] == process_date3[0]:
                        print(transaction)
                    else:
                        break
                else:
                    break
            else:
                break

    def __handle_cardclient_remove(self):
        """
        Removes the client' card in every transaction that it shows up
        """
        try:
            id_cardclient = input('Give the ID that you would like to remove: ')
            while type(id_cardclient) is not int:
                try:
                    id_cardclient = int(id_cardclient)
                except ValueError:
                    print("The ID must be a natural number")
                    id_cardclient = input("Give the ID that you would like to remove : ")
            self.__card_client_service.remove_card_client(id_cardclient)
            print("The Card Client with the given ID has been successfully removed")
            for transaction in self.__transaction_service.get_all():
                if transaction.id_card_client == id_cardclient:
                    self.__transaction_service.remove_transaction(transaction.id_entity)
                    print("The transaction has been succesfully removed!")
        except ValueError:
            print("The ID is wrong")
        except ServiceError:
            print("There is no card client with the given id!")