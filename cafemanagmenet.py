#define the menu of restarurant

menu={
    'pizza' : 180,
    'radsospasta' : 70,
    'whitesospasta' : 70,
    'burger' : 40,
    'sendwhich' : 60,
    'peties' : 30,
    'dosa' : 120,
}

print("Welcome to PYTHON Restarurant")
print("pizza: Rs. 180\n rad sos pasta: Rs. 70\n Wthite sos pasta: Rs. 70\n Burger: Rs. 40\n sendwhich: Rs. 60\n Peties: Rs.30\n dosa: Rs. 120 ")

order_total= 0

item_1=input("enter the name of item you want order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print("your item {item_1} has been added to your order")

else:
    print("ordred item {item_1} is not avaialable yet !")

another_order= input("Do you want to add another item ? (Yes/No)")  
if another_order == "Yes":
    item_2= input("Enter the name of second item ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item [item_2] has been added to order")
    else:
        print("ordered item {item_2} is not available !") 

print(f"The total amount of items to pay is {order_total}")




