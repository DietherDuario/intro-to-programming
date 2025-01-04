sandwhich_orders = ["Grilled cheese", "Ham and cheese", "Beef", "Vegetable"]
finished = []

while sandwhich_orders:
    making = sandwhich_orders.pop()
    print("Currently making your" + making + " sandwhich.")
    finished.append(making)

for sandwhich in finished:
    print("Your" + sandwhich + "sanwhich. Enjoy!")
    