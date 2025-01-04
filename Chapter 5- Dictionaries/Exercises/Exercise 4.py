rivers = {
    "Nile": "Egypt",
    "Amazon River": "Brazil",
    "Yangtze River": "China",
    "Danube River": "Austria",
    "Rhine River": "Germany",
    }

for river, country in rivers.items():
    print("The " + river + " flows in the country of " + country + ".")

print("\nThe rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river)

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country)