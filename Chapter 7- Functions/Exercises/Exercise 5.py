def describe_city(city, country="Philippines"):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city("Manila")
describe_city("Davao")
describe_city("Abudhabi", "United Arab Emirates")