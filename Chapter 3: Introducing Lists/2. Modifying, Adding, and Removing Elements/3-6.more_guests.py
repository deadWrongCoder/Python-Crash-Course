guest_list = ["Albert Einstein", "Richard Feynman", "Niels Bohr"]
print(f"You've been invited to the dinner, {guest_list[0]} ")
print(f"You've been invited to the dinner, {guest_list[1]} ")
print(f"You've been invited to the dinner, {guest_list[2]} ")
print(f"{guest_list[2]} can't make it.")
guest_list[2] = "Ernest Rutherford"
print(f"You've been invited to the dinner, {guest_list[0]} ")
print(f"You've been invited to the dinner, {guest_list[1]} ")
print(f"You've been invited to the dinner, {guest_list[2]} ")
print(f"I found a bigger dinner table, {guest_list[0]}, {guest_list[1]}, {guest_list[2]}")
guest_list.insert(0, "Michael Faraday")
guest_list.insert(3, "Isaac Newton")
guest_list.append("Galileo Galilei") #or guest_list.insert(6, "Galileo Galilei")
print(f"You've been invited to the dinner, {guest_list[0]} ")
print(f"You've been invited to the dinner, {guest_list[1]} ")
print(f"You've been invited to the dinner, {guest_list[2]} ")
print(f"You've been invited to the dinner, {guest_list[3]} ")
print(f"You've been invited to the dinner, {guest_list[4]} ")
print(f"You've been invited to the dinner, {guest_list[5]} ")
