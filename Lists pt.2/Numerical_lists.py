#USE LOOP TO PRINT THE SET OF NUMBERS IN A LIST USING RANGE
#It only prints the value that goes from the first to the second to last number.
for number in range (1,5):
	print(number)			

#CREATE A LIST OF NUMBER USING RANGE AND LIST FUNCTIONS
numbers = list(range(1,11))
print("\n" + str(numbers))

#CREATE A LIST OF EVEN NUMBERS
#specifies the range between 2 and 20. Then takes considers values every 2 numbers (third specifica)
even_numbers = list(range(2,20,2))   
print("\n" + str(even_numbers))     

#CREATE A LIST THAT INCLUDES THE SQUARES OF A SPECIFIC NUMBER WITHIN A CERTAIN RANGE
lista_cubi = []   

for valori in range(1,10):        #considero i valori nel range 1-19
	valore_al_cubo = valori**3     #creo variabile "valore al cubo" che è uguale a il valore del loop elevato al cubo  
	lista_cubi.append(valore_al_cubo)    #aggiungo alla lista il valore del loop elevato al cubo.

print("\n" + str(lista_cubi))

#SIMPLE STATISTICS WITH LISTS OF NUMBERS
lista_numeri = list(range(1,10))        #creo lista_numeri con list e range functions

print("\n Minimo = " + str(min(lista_numeri)))    #trovo il minimo valore
print("\n Massimo = " + str(max(lista_numeri)))    #trovo il massimo valore
print("\n Somma = " + str(sum(lista_numeri)))    #trovo la somma dei valori

#CREATE A LIST COMPREHENSION
cubi = [value**3 for value in range(1,10)]    #this is a faster way to create a list, similar to the square excercise but with a single line of code.
print("\n" + str(cubi))