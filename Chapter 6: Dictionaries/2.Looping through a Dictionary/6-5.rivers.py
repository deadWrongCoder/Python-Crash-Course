rivers = {
    "nile": "egypt",
    "amazon" : "peru",
    "ob": "russia"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
