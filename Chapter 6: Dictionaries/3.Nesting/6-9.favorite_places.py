cities ={
    "Polly": ["Paris", "Nice", "Bordeaux"],
    "Jenny": ["New York", "Washington"],
    "Elisabeth": ["Dublin"]
}

for person, places in cities.items():
    print(f"{person}'s favorite cities are: ")
    for city in places:
        print(f"{city}")
