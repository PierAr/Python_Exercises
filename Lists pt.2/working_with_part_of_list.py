#SLICING A LIST
lista_numeri=list(range(1,11))     #creates numbered list with list and range functions
print(lista_numeri[0:3])		   #prints the list but only for the first 3 numbers

#SLICE FROM POINT A TO THE END
lista_nomi = ["Andrea", "Giacomo", "Antonio", "Claudio", "Gianluigi"]
print(lista_nomi[3:]) #prints from name number 4 to the end.

#LOOPING THROUGH A SLICE
lista_numeri=list(range(1,50))

for numero_in_range in lista_numeri[9:51]:
	print(numero_in_range)

#COPYING LISTS
my_food = ["Eggplant", "Pizza", "Salame"]
ally_food = my_food[:]                    #create a list that is exactly the same as my_food

print("My favorite food are:")
print(my_food)

print("\n Ally's favorite food are:")
print(ally_food)							#print to check that they are all the same

my_food.append("cozze")				#add 2 different things to the two lists
ally_food.append("pasticio")

print("\n My favorite food are:")
print(my_food)

print("\n Ally's favorite food are:")
print(ally_food)