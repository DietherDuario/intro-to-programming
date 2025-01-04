prompt = "What is your age?"
prompt += "Kindly enter 'quit' when you're done! "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get will be free!")
    elif age < 13:
        print("  Your ticket will be $10!")
    else:
        print("  Your ticket will be $15!")