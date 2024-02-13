
client_name ="John Doe"
client_account_nr="12345678"
client_balance_amount = 1000_00
current_balance_currency="USD"

client={
    "name" : "John Doe",
    "acc" : "2301231321321",
    "balance_amount" : 1000_00, #cents
    "balance_currency":"USD"
    
}


client['card_number'] = "1234"

client['PIN'] = "1234"

card_number_ext=input("What is your card number? ")
if card_number_ext==client["card_number"]:
    pin_ext=input("Existing card.\nWhat is your pin? ")
    if pin_ext==client["PIN"]:
        sum_money=int(input("money: ")) * 100
        client["balance_amount"]+=sum_money

print(client["balance_amount"])

        






#HW1 - based on the data scruture above, continue this app: 
        # - introduce money
        # - ask and confirm the card number
        # - ask and confirm the PIN code
        # - update the amount to the account (*100)

#HW2*: add interactivity 
#      - menu 1. to check balance 2. to take out money 
#             3. change pin 4. and so on...  
