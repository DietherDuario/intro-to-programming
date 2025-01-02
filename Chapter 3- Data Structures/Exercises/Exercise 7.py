Places = ["Hamdan Center", "Disney World", "Hawaii", "Bahamas", "Korea"]

print("Same Order:")
print(Places)

print("\nAlphabetical:")
print(sorted(Places))

print("\nSame Order:")
print(Places)

print("\nReverse alphabetical:")
print(sorted(Places, reverse=True))

print("\nSame Order:")
print(Places)

print("\nReversed:")
Places.reverse()
print(Places)

print("\nSame Order:")
Places.reverse()
print(Places)

print("\nAlphabetical")
Places.sort()
print(Places)

print("\nReverse alphabetical")
Places.sort(reverse=True)
print(Places)