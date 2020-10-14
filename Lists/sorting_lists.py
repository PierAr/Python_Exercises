
#sort a list alphabetically with sort()
lettere=["c","b","a","f","k"]
print(lettere)

lettere.sort()   #sort orders in an irreversible order
print(lettere)

#sort list in reverse alphabetical order
lettere.sort(reverse=True)
print(lettere)

#sort a list alphabetically with a non-irreversible function
original_order = lettere
new_order = sorted(lettere)
print("\n This is the original list order" +"\n" +str(original_order))
print ("\n This is the new order" + "\n" + str(new_order))
print("\n This is the original order again" + str(original_order))

#Print a list in reverse order. NOT in reverse alphabetical order.
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("\n" + str(weekdays))
weekdays.reverse()
print(weekdays)

#Find the lenght of a list
len(weekdays)
print("\n" + str(len(weekdays)))