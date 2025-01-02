guests = ["Nyjah Huston", "Yuto Horigome", "Bill Gates", "Thomas the tank engine"]

name = guests[0]
print(name + ", You're invited to the dinner!.")

name = guests[1]
print(name + ", You're invited to the dinner!.")

name = guests[2]
print(name + ", You're invited to the dinner!.")

name = guests[3]
print(name + ", You're invited to the dinner!.")

name = guests[2]
print("Sadly," + name + " Cannot attend dinner with us.")

del(guests[2])
guests.insert(2, "Jackie Chan")

name = guests[0]
print(name + ", You're invited to the dinner!.")

name = guests[1]
print(name + ", You're invited to the dinner!.")

name = guests[2]
print(name + ", You're invited to the dinner!.")

name = guests[3]
print(name + ", You're invited to the dinner!.")

print("\nLooks like we can only invite 2 people.")

name = guests.pop()
print("Very unfortunate, " + name + " you've been removed from the dinner!")

name = guests.pop()
print("Very unfortunate, " + name + " you've been removed from the dinner!")

name = guests[0]
print(name + ", You're still invited")

name = guests[1]
print(name + ", You're still invited")

del(guests[0])
del(guests[0])
print(guests)