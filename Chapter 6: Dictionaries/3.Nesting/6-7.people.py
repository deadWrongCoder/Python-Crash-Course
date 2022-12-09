person1 = {"name": "Lawrence", "lastname": "Krauss", "age": "68", "country": "USA"}
person2 = {"name": "Richard", "lastname": "Dawkins", "age": "81", "country": "Great Britain"}
person3 = {"name": "Robert", "lastname": "Sapolsky", "age": "65", "country": "USA"}
people = [person1, person2, person3]

for person in people:
    print(f"{person['name']} {person['lastname']} is {person['age']} years old. He currently lives in {person['country']}. ")
