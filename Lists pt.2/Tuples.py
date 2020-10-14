# CREATE AN IMMUTABLE LIST (TUPLE)
dimensions = (200,50,30,70) # list is immutable if you use ()
print(dimensions[1])	# BUT when you print and select items use []
print(dimensions[3])

# WRITING OVER A TUPLE
names = ("Pier", "Antonio", "Marcello")  #create original tuple
print("\nThe original name list is:")
for single_name in names:                #use loop to print all names.
	print(single_name)

names = ("Claudio", "Tobia", "Fernando")
print("\nThe new name list is")
for single_name in names:
	print(single_name)
