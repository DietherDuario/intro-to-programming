pets = []

pet = {
    "Animal": "Snake",
    "Name": "Earl",
    "Owner": "Gian",
    "Weight": 24,
    "Eats": "Small bugs",
}

pets.append(pet)

pet = {
    "Animal": "Cat",
    "Name": "Sandstorm",
    "Owner": "Tj",
    "Weight": 14,
    "Eats": "Chicken"
}

pets.append(pet)

pet = {
    "Animal": "Dog",
    "Name": "Poppy",
    "Owner": "Ray",
    "Weight": 26,
    "Eats":"Bones"
}

pets.append(pet)

for pet in pets:
    print(f"Here's what we know about the! {pet["Name"].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")