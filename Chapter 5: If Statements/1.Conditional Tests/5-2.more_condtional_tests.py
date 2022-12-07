# Conditional test with strings

string1 = "hello"
string2 = "BYE"
print(string1 == "hello")
print(string2 == "bye")

# Case-insensitive tests with strings

string1 = "hello"
string2 = "BYE"
print(string1.lower() == "hello")
print(string2.lower() == "bye")

# List tests

list = [1, 2, 3, 4, 5, 7]

print(1 in list)
print(6 in list)
print(7 not in list)
print(10 not in list)
