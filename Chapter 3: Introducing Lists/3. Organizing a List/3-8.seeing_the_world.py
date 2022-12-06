places = ["Machu Picchu", "Volcanoes of Kamchatka", "Ireland", "Japan", "Silicon Valley"]
print(places)

# Alphabetical ordered list
print(sorted(places))

# Original list hasn't changed
print(places)

# Reverse alphabetical ordered list
print(sorted(places, reverse=True))

# Original list hasn't changed
print(places)

# Original list was reversed

places.reverse()
print(places)

# Original list was reversed again

places.reverse()
print(places)

# Alphabetical ordered list
places.sort()
print(places)

# Reverse alphabetical ordered list

places.sort(reverse=True)
print(places)
