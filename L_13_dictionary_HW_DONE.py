import os
import time

client_name = "John Doe"
client_account_nr = "12345678"
client_balance_amount = 1000_00
current_balance_currency = "USD"

client = {
    "name": "John Doe",
    "acc": "2301231321321",
    "balance_amount": 1000_00,  # cents
    "balance_currency": "USD"
}

client['card_number'] = "1234"
client['PIN'] = "1234"

user_input = True
guess_pin = 3
guess_card = 3

while True:
    print()
    print("                 ------WELCOME TO THE ATM---------")
    print()
    user_card_number = input("What is your card number? ")
    if user_card_number == client["card_number"]:
        while guess_pin > 0:
            user_pin = input("What is your pin code? ")
            if user_pin == client["PIN"]:
                while user_input:
                    os.system("cls")
                    print("        -#-#-#-#- Access granted -#-#-#-#-")
                    user_request = input("""
        1. Press 1 to check balance
        2. Press 2 to take out money
        3. Press 3 to change your PIN code
        4. Press 4 to add money 
        5. Press q to quit                         
        """)

                    if user_request == '1':
                        print(client["balance_amount"]/100,"$")
                        user_input = input("Any other actions? (y/n) ").lower() == 'y'
                    elif user_request == '2':
                        print("You have", {client["balance_amount"] / 100}, "$")
                        amount_to_take = int(input("How much money you want to take out? ")) * 100
                        if amount_to_take <= client["balance_amount"]:
                            print(f"wait for the ATM to count out {amount_to_take / 100}$")
                            time.sleep(2)
                            client["balance_amount"] -= amount_to_take
                            print("your remaining amount is ", {client["balance_amount"] / 100}, "$")
                            user_input = input("Any other actions? (y/n) ").lower() == 'y'
                        else:
                            print("non-sufficient funds")
                    elif user_request == "3":
                        user_pin = input("one more time your old PIN code please")
                        if user_pin == client["PIN"]:
                            client["PIN"] = input("Enter your new PIN ")
                            print(client["PIN"], "is your new PIN code ")
                            user_input = input("Any other actions? (y/n) ").lower() == 'y'
                        else:
                            print("Goodbye, schemer")
                            time.sleep(2)
                            os.system("cls")
                            user_input = False
                    elif user_request == "4":
                        add_money = int(input("How much $ you want to add? "))*100
                        client["balance_amount"] += add_money
                        print(client["balance_amount"]/100, "is your new balance")
                        user_input = input("Any other actions? (y/n) ").lower() == 'y'
                    elif user_request=="q":
                        print("Bye,Bye")
                        print()
                        break
                    
                break
            else:
                guess_pin -= 1
                if guess_pin == 0:
                    print("You are out of PIN tries")
                    break
                else:
                    print(f"Incorrect PIN. {guess_pin} more tries remaining.")
        break
    else:
        guess_card -= 1
        if guess_card == 0:
            print("You are out of card number tries")
            break
        else:
            print(f"Incorrect card number. {guess_card} more tries remaining.")
        






#HW1 - based on the data scruture above, continue this app: 
        # - introduce money
        # - ask and confirm the card number
        # - ask and confirm the PIN code
        # - update the amount to the account (*100)

#HW2*: add interactivity 
#      - menu 1. to check balance 2. to take out money 
#             3. change pin 4. put in money 
