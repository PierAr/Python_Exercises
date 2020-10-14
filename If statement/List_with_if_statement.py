#IF ELIF ELSE STATEMENTS

salary = 4000

if salary <1000:
	print("Prendi poco")
elif salary >= 1000 and salary < 3000:		#as many ELIF as the user wants.
	print("Sei nella media")				#works only if you need 1 single condition to be satisfied.
elif salary >= 3000 and salary<5000:
	print("Prendi abbastanza")
else:
	print("Prendi molto")

#IF STATEMENTS IN LISTS
print("\n")	
ingredienti =["faRina", "Salame", "acqua", "suGo", "mErda"]											

for ingrediente in ingredienti:			#loops ingredients and prints them
	if ingrediente.lower() == "merda":
		print("Sorry we do not have " + str(ingrediente.lower()) + " today")
	else:
		print("Abbiamo " + str(ingrediente.lower()))

#CHECK IF LIST IS NOT EMPTY
print("\n")
ingredienti =["faRina", "Salame", "acqua", "suGo", "mErda"]	

if ingredienti:											#This tells python to see if the list has an item (1+ items = TRUE).. 
	for ingrediente_richiesto in ingredienti:
		if ingrediente_richiesto.lower() == "merda":
			print("Sorry I don't have " + str(ingrediente_richiesto).lower())
		else:
			print("Aggiungiamo questo ingrediente: " + str(ingrediente_richiesto).lower())
else:
	print("Sicuro di volere una pizza senza nulla?")

#USE OF MULTIPLE LISTS 
print("\n")

available_toppings = ["salaMe", "mozzarella", "stracciatella", "mushrooms", "bacon"]
requested_toppings = ["sALame", "musHrooms", "parmigiano"]

for topping_index in range(0,len(available_toppings)):								#make every item in available toppings lower case
	available_toppings[topping_index] = available_toppings[topping_index].lower()

for requested_index in range(0,len(requested_toppings)):							#make every item in requested toppings lower case
	requested_toppings[requested_index] = requested_toppings[requested_index].lower()

for requested_topping in requested_toppings:										#check wheter item requested is in the topping list or not
	if requested_topping in available_toppings:
		print("Adding the requested topping: " + str(requested_topping))
	else:
		print("The " + str(requested_topping) + " is not available, sorry")
print("\nFinished making your pizza.")







