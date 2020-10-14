#create and print a list
first_names = ["pier", "allyson", "tony", "kevin", "paolo"]
print(first_names)

#print a specific list item --> list number starts from 0
print(first_names[1].title())
print(first_names[3].title())
#calling for item in -1 position gives bacj the last item
print(first_names[-1].title())

#use item in a list as normal values
print(("\nmy name is ").title() + first_names[0].title())

#change values in a list
cities = ["Berlin", "Budapest", "Roma", "Milano"]
print(cities)

cities[0] = "Reggio Emilia"
print(cities)










