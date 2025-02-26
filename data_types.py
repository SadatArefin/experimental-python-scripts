girl_names = ['Alice', 'Anna', 'Sofia', 'Emma', 'Olivia', 'Mia', 'Isabella', 'Zoe', 'Lily', 'Emily']
boy_names = ['Liam', 'Noah', 'William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas', 'Mason', 'Logan']

# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    # print(f'Rank {rank+1}: {girl_name} and {boy_name}')

cookie_name = "Anzac"
cookie_price = "$2.58"

# print(f"{cookie_name} cookies are {cookie_price}.")

child_ages = ["12", "8", "14", "7", "6", "10", "5", "9", "13", "11"]
# print(", ".join(child_ages))

# print(f"The children are ages {', '.join(child_ages[0:-1])} and {child_ages[-1]}.")

art_galleries = { 
    "National Gallery of Art": "Washington, D.C.", 
    "Museo del Prado": "Madrid", 
    "Louvre": "Paris", 
    "Tate Modern": "London", 
    "Museum of Modern Art": "New York City", 
    "Uffizi Gallery": "Florence", 
    "Rijksmuseum": "Amsterdam", 
    "National Gallery": "London", 
    "Whitney Museum of American Art": "New York City", 
    "British Museum": "London",
    "Museum of Fine Arts": "Boston",
    "Metropolitan Museum of Art": "New York City",
    "Art Institute of Chicago": "Chicago",
    "State Hermitage Museum": "St. Petersburg",
    "Guggenheim Museum": "New York City",
    "Palace of Versailles": "Versailles",
    "National Portrait Gallery": "London",
    "Museum of Contemporary Art": "Chicago",
    "Tate Britain": "London",
    "Centre Pompidou": "Paris",
    "Museum of Fine Arts": "Houston",
    "Philadelphia Museum of Art": "Philadelphia",
    "Museum of Fine Arts": "Montreal"}

# for name in sorted(art_galleries)[-8:-2]:
    # print(name)
    # pass

# print(art_galleries.get("Museum of Fine Art", "Not Found"))
# print(art_galleries.get("Museum of Modern Art", "Not Found"))
# print(art_galleries.get("Museum of Fine Art"))

galleries_11234 = [('A J ARTS LTD', '(718) 763-5473'),
                   ('Doug Meyer Fine Art', '(718) 625-2823'),
                   ('Gallerie Icosahedron', '(718) 797-3111')]
art_galleries['11234'].update(galleries_11234)
print(art_galleries['11234'])