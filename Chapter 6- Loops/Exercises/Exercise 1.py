prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    toppings = input(prompt)
    if toppings != 'quit':
        print("We will be adding " + toppings + " to your pizza!")
    else:
        break