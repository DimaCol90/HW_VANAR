#food order

order = {
    "client": "John Doe",
    "item"  : "Salad",
    "quantity":int(input(f"How many pieces of food do you need? ")),
    "price":15.00
}



if order["quantity"]<7:
    discount=1
else:
    discount=0.8
    

order['total']=(order["quantity"]*order['price'])*discount

delivery_wanted=input("Do you need delivery?(y/n)")=="y"
if delivery_wanted and order["total"]>300:
    order['delivery']='Free'
elif delivery_wanted and order["total"]<300:
    order['delivery']=50.00
    order['total']+=order['delivery']    


print("ORDER for:",order["client"])
print("Food:",order["item"])
print("discount=",100-(discount*100),"%")
print("price x qty:",order["price"],'x',order['quantity'],'+',order["delivery"],'=',order['total'])

#HW discount order when quantity is > 7
#HW add code so the USER can input answer to delivery
#   based on the answer: total > 300.00 and the user asked for delivery
# include in dictionary order['delivery']="Free"
# otherwise, if delivery needed -> order["delivery"]=50.00 and order['total'] updated
