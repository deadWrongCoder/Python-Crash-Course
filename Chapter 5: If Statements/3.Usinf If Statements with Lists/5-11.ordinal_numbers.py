numbers = [value for value in range(1, 10)]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2 or number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
