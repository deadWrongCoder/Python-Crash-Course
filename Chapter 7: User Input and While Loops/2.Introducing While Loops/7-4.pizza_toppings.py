flag = True
toppings = []
while flag:
    topping = input("What topping do you want to add? ")
    if topping == "quit":
        break
    else:
        toppings.append(topping)
        print(f"You've add {topping}")
