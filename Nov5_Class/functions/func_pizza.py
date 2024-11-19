def pizza_toppings(*toppings):
    print(toppings) #tuple or list
    for i in toppings:
        print(i)

print("Supreetha's pizza toppings")
sup=pizza_toppings("Onion", "corn", "paneeer","capsicum")
print("Shreshta's pizza toppings")
shreshtu=pizza_toppings("extracheese", "paneer", "onion")