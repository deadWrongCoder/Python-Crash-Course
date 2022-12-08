users = ["admin", "Albert", "Richard", "Charles", "Lawrence"]


for user in users:
    if user == "admin":
        print(f"Hello {user}, would you like to see a status report? ")
    else:
        print(f"Hello {user}, thank you for logging in again.")

users = []

if users:
    pass
else:
    print("We need to find some users!")
