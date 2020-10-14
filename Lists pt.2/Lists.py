
#Use for function to extract items from list automatically ---> TO CREATE A LOOP
weekdays=["monday","tuesday","wednesday","thursday","friday", "saturday", "sunday"]
last_day = weekdays.pop()
for name_of_day in weekdays:    #create a loop where for every name of day in the list weekdays the program prints the items in the list.
	print(name_of_day.title() + " is a pretty good day.")
	print("Although I have to say that the next one is a bit better because it is closer to " + str(last_day)+".\n")

print("I hate " + str(weekdays[0] + " because I have to start working but I love " + str(last_day) + " because I relax"))   #ONCE INDENT IS OVER, LOOP IS OVER.