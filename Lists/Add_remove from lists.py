#Add values to a list    [append]
cities = ["Berlin", "Budapest", "Roma", "Milano"]
cities.append ("Bologna")
print(cities)

#Create empty list and add items    
oggetti =[]
oggetti.append("telefono")
oggetti.append("tovaglia")
oggetti.append("gamba")
print(oggetti)

#add item in a list into a specific position    [Insert]
oggetti.insert(1, "computer")
print(oggetti)

#delete item from list if you know the position    [del]
del oggetti[0]
print(oggetti)

#removing items using the pop method and keeping them in the log
programmi_tv = ["simpsons", "futurama", "family guy", "narcos"]
print("\n" + str(programmi_tv))

popped_programmi_tv = programmi_tv.pop()      #create a variable that is equal to the value that you are going to pop
print("\n" + str(programmi_tv))
print(popped_programmi_tv)

#Popping items at any point in a list with pop
programmi_tv.append(popped_programmi_tv)      #re add the popped value to create the initial list that we had above
favorite_show = programmi_tv.pop(1)           #use pop to choose the one that I think is my favorite and equate to favorite_show
print("\n" + "My favorite tv show is " + favorite_show.title())

#Remove item by value if position is unkown
programmi_tv.append(favorite_show)     #add back the value i popped previously
programmi_tv.remove("futurama")        #remove the value again by using remove
print ("\n" + str(programmi_tv))