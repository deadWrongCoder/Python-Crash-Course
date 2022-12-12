flag = True

while flag:
    age = int(input("What's your age? "))
    if age <3:
        print("Your ticket is free. ")
    elif 3<= age <= 12:
        print("You need to pay $10. ")
    else:
        print("You need to pay $15. ")

