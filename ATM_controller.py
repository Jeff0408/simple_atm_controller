import sys

class Bank:
    def __init__(self):
        self.bank_data = {}

    def add_entry(self, card_num, pin, account, amt):
        self.bank_data[card_num] = {"pin":pin, "account":{account:amt}}

    def add_account(self, card_num, account, amt):
        if card_num in self.bank_data:
            self.bank_data[card_num]["account"][account] = amt

    def check_pin(self, card_num, entered_pin):
        if card_num in self.bank_data and self.bank_data[card_num]["pin"] == entered_pin:
            return self.bank_data[card_num]["account"]
        else:
            return None

    def data(self, data):
        data = {}
        data = self.bank_data
        return data

class Controller:
    def __init__(self, bank, cash):
        self.Bank = bank
        self.accounts = None
        self.cash_bin = cash

    def insert_card(self, card_num, pin):
        self.accounts = self.Bank.check_pin(card_num, pin)
        if self.accounts is None:
            return 0, "Invalid Card or Incorrect Pin!"
        else:
            return 1, "Welcome!"

    def account_select(self, acc):
        if acc in self.accounts:
            return True
        else:
            return False

    def account_actions(self, card_num, acc, action, amt):
        if action == "See Balance":
            return self.accounts[acc], 1
        elif action == "Withdraw":
            if self.accounts[acc] >= amt and self.cash_bin >= amt:
                self.cash_bin += amt
                self.accounts[acc] -= amt
                return self.accounts[acc], 1
            elif self.accounts[acc] < amt:
                print("\nLess than", amt, "in your account, cannot withdraw")
            else:
                return self.accounts[acc], 0
        elif action == "Deposit":
            if self.cash_bin < amt:
                print("\nYou don't have enough cash to deposit")
            else:
                self.cash_bin -= amt
                self.accounts[acc] += amt
                return self.accounts[acc], 1
        else:
            print("try again")
            return self.accounts[acc], 2
        
    def cash_info(self):

        print("\ncash in your wallet : ",self.cash_bin, "\n")


if __name__ == "__main__":

    if sys.version_info < (3, 7, 2):
        sys.exit("Please use Python 3.7.2")
    print("this is a simple ATM controller project\n" )
    # Generating an interesting bank
    #setting your card information
    card_number1 = 123456789
    pin_number1 = 1234
    #setting your bank
    bank1 = Bank()
    bank1.add_entry(card_number1, pin_number1, "checking", 1000)
    bank1.add_account(card_number1, "savings", 1000)
    '''
    #setting second card
    card_number2 = 987654321
    in_number2 = 4321
    bank1.add_entry(card_number2, pin_number2, "checking", 5000)
    '''
    
    #initialize
    data = {}
    data = bank1.data(data)

    atm1 = Controller(bank1, 10000)
    atm1.cash_info()
    
    #start ATM controller
    print("please insert your card\n")
    r = 0
    while True:
        input_card_num = int(input("card_num : "))
        input_pin = int(input("pin : "))
        print("")
        r = atm1.insert_card(input_card_num, input_pin)[0]
        if r == 0:
            print(atm1.insert_card(input_card_num, input_pin)[1])
            print("please try again")   
            continue
        else:
            print(atm1.insert_card(input_card_num, input_pin)[1])
            print("")
            break
    
    print("account list : \n")
    print(data[card_number1]['account'])
    
    while True:
        acc = input("account : ")
        check = atm1.account_select(acc)
        if check is False:
            print("Invalid Account!")
            print("please try again (checking or savings)")
        else:
            print("\nEntering your", acc, "account now !")
            break
        
    while True:
        action = input("choose your action : Leave, See Balance, Withdraw, Deposit : ")
        if action == "Leave":
            print("Gracefully departed")
            break
        
        elif action == "See Balance" :
            amount = 0
            print("\nBalance : ", atm1.account_actions(input_card_num, acc, action, amount)[0])
            atm1.cash_info()
            
        elif action == "Withdraw":
            input_amount_w = int(input("amount : "))
            atm1.account_actions(input_card_num, acc, action, input_amount_w)
            print("\nBalance : ", atm1.account_actions(input_card_num, acc, action, amount)[0])
            atm1.cash_info()
        elif action == "Deposit":
            input_amount_d = int(input("amount : "))
            atm1.account_actions(input_card_num, acc, action, input_amount_d)
            print("\nBalance : ", atm1.account_actions(input_card_num, acc, action, amount)[0])
            atm1.cash_info()
        else:
            print("\ntry again")
            continue

