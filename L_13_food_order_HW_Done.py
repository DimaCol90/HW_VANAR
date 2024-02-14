#order info -> lists

order_food_name=["Pizza","Salad","Soup"]
order_food_price=[75.00,45.00,15.00]
order_food_q=[2,1,2]
order_food_total=[]
#iterative print

for i in range(len(order_food_name)):
    order_food_total.append(order_food_price[i]*order_food_q[i])
    print(i,".", order_food_name[i],"x",order_food_price[i],"x",order_food_q[i],"=",order_food_total[i])



#HW2: total