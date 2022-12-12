sandwich_orders = ["cheese sandwich", "ham sandwich", "tuna sandwich"]

finished_orders = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_orders.append(sandwich)

for order in finished_orders:
    print(f"Finished order: {order}")

