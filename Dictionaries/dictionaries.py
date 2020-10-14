#CREATE A BASIC DICTIONARY
alien_0 = {"color": "Green", "points": "5"}   #parentesi graffa

print(alien_0["color"])							   
print(alien_0["points"])

#ADD KEY-VALUE POINTS TO A DICTIONARY
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

#START WITH EMPTY DICTIONARY AND FILL IT UP
alien_0 = {}
alien_0["strenght"] = 20
alien_0["points"] = 45
print("\n")
print(alien_0)

#CHANGE VALUES IN A DICTIONARY
print("\n")
alien_0 = {}  #create dictionary

#create color key and set original alien color to green
alien_0["color"] = "Green"										
print("The original color of the alien is " + alien_0["color"])

#change alien color to red
alien_0["color"] = "Red"										
print("The new color of the alien is " + alien_0["color"])

#ALIEN SPEED EXAMPLE
#create the alien position and assign a speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print("\nThe original x position of the alien is " +str(alien_0["x_position"]))

#Move the alien to the right (x-axis) and determine the speed
if alien_0['speed'] == 'slow':
	x_increment = 1 
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

#the new position is the old one + the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment
print("\nThe new x position of the alien is " + str(alien_0["x_position"]))

#REMOVING KEY VALUE PAIRS
alien_0 = {"color" : "green", "points" : 5}
print(alien_0)

del alien_0["color"]
print(alien_0)

