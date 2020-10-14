
#concatenate parts of texts and variables and 
#eliminate whitespaces by using the strip() function.
first_name = "Pier      "
print("Se " + first_name.title().strip() + " " + "impara Python e SQL diventa un analista molto interessante")

#use upper, lower and title functions to cap or uncap strings
print("\n" + first_name.title())
print(first_name.upper())
print(first_name.lower())

#use \n and \t to manage spacing in text and concatenate strings and variables
author_name = "Un cieco"
message =("\n\t"  + author_name.title() + " " + "disse: celosidovevasiaspettarselo")
print(message)

#Use strinf fuction to make sums work and display correctly
print ("\n" + str(5+3))

#concatenate + use string and combine with .title() to view print text correctly.
favorite_number = 75
print("\nmy ".title() + "favorite number is " + str(favorite_number))

