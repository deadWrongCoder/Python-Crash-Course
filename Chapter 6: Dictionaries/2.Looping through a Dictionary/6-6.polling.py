favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ["jen", 'edward', "toby", "michael"]

for person in people:
    if person in favorite_languages:
        print(f"{person.title()}, thank you for responding. Your favorite language is {favorite_languages[person].title()}.")
    else:
        print(f"{person.title()}, we've invited you to take this poll. ")
