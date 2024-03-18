from json import loads
from restaurant import *


order = {
    "items":[]
}
food=loadFood()
while True:
    option = printMenu()
    if option==0:
        break
    elif option==1:
        printFood(food)
        input("Hit enter to continue ")
    elif option==2:
        selected_i=int(input("which item: ")) - 1
        print(f"You've selected - <<{food[selected_i]['name']}>>")
        quantity=int(input("How many? "))
        
        
        if quantity>food[selected_i]["avail"]:
            print(f"We don't have this quantity, we can only serve {food[selected_i]['avail']} pieces of {food[selected_i]['name']}")
            agreed_q=input("Do you agree?(y/n)")=="y"
            if agreed_q:
                quantity=food[selected_i]["avail"]

        price_per_item=quantity*food[selected_i]['price']['amount']
        print(f"<<{food[selected_i]['name']}>> * {quantity} ={price_per_item:8.2f}{food[selected_i]['price']['currency']}")
        
        agreed_o=input("Would you like to proceed with the order?(y/n) ") == "y"
        if agreed_o:

            order_item = {
                "name": food[selected_i]['name'],
                "quantity": quantity,
                "total": {
                    "amount": price_per_item,
                    "currency": food[selected_i]['price']['currency']
                }
            }
            order['items'].append(order_item)
            print("Item added to order.")
        
        
        
            print("Your order:")
        for item in order['items']:
            print(f"{item['name']}: {item['quantity']} x {item['total']['amount']} {item['total']['currency']}")
        input("Hit enter to continue ")
