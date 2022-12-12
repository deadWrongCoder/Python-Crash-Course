sandwich_orders = ["cheese sandwich", "pastrami", "pastrami", "ham sandwich", "tuna sandwich", "pastrami"]


print("We're sorry but the deli is run out of pastrami. ")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)
