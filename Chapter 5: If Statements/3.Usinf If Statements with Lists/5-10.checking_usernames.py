current_users = ["admin", "Albert", "Richard", "Charles", "Lawrence"]
new_users = ["ADMIN", "Nicole", "Florence", "George"]

for user in new_users:
    if user.lower() in current_users:
        print(f"{user}, You need to enter a new username! ")
    else:
        print(f"username {user} is available. ")
