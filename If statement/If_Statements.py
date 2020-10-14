#------------------------------------------------------------CREATE A SIMPLE IF STATEMENT IN A LOOK------------------------------------------------------------

cars = ["audi", "bmw", "ferrari", "volkswagen"]

for brand in cars:
    if brand == "bmw" :       #note syntax "==" and ":      
        print(brand.upper())  #--> executed only in case IF statement is TRUE.
    else:                     #note syntax ":"
        print(brand.title())

#-----------------------------------------------TAKE CASE SENSITIVE CONDITIONALITY AWAY (IF STATEMENT IS CASE SENSITIVE BY DEFAULT)------------------------------------------------------------------------------------------
car = "BmW"
check_car = "BMW"

if check_car.lower() == car.lower() :      #telling the program that can't be case sensitive
    print("\nIf statement con lower works\n")

#----------------------------------------------------CHECK IF ONE NAME DOES NOT APPEAR IN A LIST WITH THE CAPS TWIST  ---------------------------------------------------------------------------------------------------------
objects = ["tavOlo", "sEdia", "Bottiglia", "PIATTO", "bicchiere", "LAVandino"] #create list
target_object = "lavanDino" #create target object to search in the list

for item_position in range(0,len(objects)):   #create loop that creates item_position as number that goes from 0 to the lenght of the objects list
    objects[item_position] = objects[item_position].lower() #substitute the item in the list that corresponds to the loop position with the same object but with lower case


if target_object.lower() in objects:            #if target object is in the list objects
    print("There is a lavandino in the list")   #then print that
else:                                           #otherwise
    print("There is no lavandino in the list\n")  #print this.
        
#------------------------------------------------------------------CHECK MULTIPLE CONDITIONS------------------------------------------------------------------------------------------------------------------------------------------------------
lista_numeri = list(range(0,15))
for numero in lista_numeri:
    if numero > 3 and numero <10:
        print("Il numero " + str(numero) + " è maggiore di 3 e minore di 10\n")
    else: 
        print("il numero " + str(numero) + " è minore di 3 o maggiore di 10 \n")

#-----------------------------------------------------------------CHECK IF VALUE IS IN A LIST-----------------------------------------------------------------------------------------------------
ingredienti = ["acQua", "saLe", "PePe", "UovO"]   #create the list
target_ingredient = "pepe"

for item_position in range(0,len(ingredienti)):                       
    ingredienti[item_position] = ingredienti[item_position].lower()   #transform all list items in lower case

if target_ingredient in ingredienti:                                  #run conditional statement that search for target ingredient in the list.
    print("Non abbiamo bisogno di comprare " +str(target_ingredient))
else:
    print("Dobbiamo comprare " + str(target_ingredient))

#-----------------------------------------------------------------CHECK IF VALUE NOT IN A LIST-----------------------------------------------------------------------------------------------------
ingredienti = ["acQua", "saLe", "PePe", "UovO"]   #create the list
target_ingredient = "terra"

for item_position in range(0,len(ingredienti)):                       
    ingredienti[item_position] = ingredienti[item_position].lower()   #transform all list items in lower case

if target_ingredient not in ingredienti:                                  #NOT IN
    print("Dobbiamo comprare " +str(target_ingredient))
else:
    print("Non dobbiamo comprare " +str(target_ingredient))

