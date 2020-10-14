#SIMPLE LOOPING
user_0 = {
	"username" : "carlom",
	"first name" : "carlo",
	"last name" : "magno",
	"email" : "aaa@gmail.com",
	"place of birth" : "sinaloa",
}
#create the loop for a dictionary
#this loop takes both key and value
for key,value in user_0.items():		
	print("\nKey: " + str(key))
	print("Value: " +str(value))

#LOOPING THROUGH ALL THE KEYS
print("\nThe program will ask the user these information:")

for ask_user in user_0.keys():
	print(ask_user.title())

#CREATE A LIST TO WORK WITH DICTIONARY
#create list to specify which data we cannot ask our users
illegal_asks = ["place of birth", "last name"]

#print which requests we cannot ask to our users
print("We can't ask the user to input this information: \n")
for ask in user_0.keys():
	if ask in illegal_asks:
		print(ask.title()) 

#delete the stored data in the dictionary to remain compliant
for item in illegal_asks:
	if item in user_0.keys():
		del user_0[item]

print(user_0)

#MAKE SURE THAT THE ORDER OF A LOOP IS ALPHABETICAL
user_0 = {
	"username" : "carlom",
	"first name" : "carlo",
	"last name" : "magno",
	"email" : "aaa@gmail.com",
	"place of birth" : "sinaloa",
}

#use sorted to return values in alphabetical order
print("\nWe ask our users the following information (in alphabetical order):")
for ask in sorted(user_0.keys()):
	print(ask.title())

#use sorted to return values in reverse alphabetical order
print("\nWe ask our users the following information (in reverse alphabetical order):")
for ask in sorted(user_0.keys(),reverse = True):        #use reverse factor in sorted formula
	print(ask.title())
		
