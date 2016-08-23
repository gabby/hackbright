selection = int(raw_input("\nSelect one: \n0 - Main Menu \n1 - Show all lists \n2 - Show a specific list \n3 - Add a new shopping list \n4 - Add an item to a shopping list \n5 - Remove an item from a shopping list. \n6 - Remove a list by nickname. \n7 - Exit when you are done.\n"))
if selection == 0: 
	print "Main Menu"
elif selection == 1:
	print "Show all lists"
elif selection == 2:
	print "Show a specific list"
elif selection == 3: 
	print "Add a new shipping list"
elif selection == 4: 
	print "Add an item to a shopping list"
elif selection == 5:
	print "Remove an item from a shopping list."	
elif selection == 6:
	print "Remove a list by nickname"
elif selection == 7: 
	print "Goodbye"
else: 
	print "You're a disappointment."
