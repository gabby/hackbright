
amazon = ["deodorant", "dish soap", "hand soap", "toilet paper"]
whole_foods = ["salmon filets", "cantaloupe", "black grapes", "zucchini"]
trader_joes = ["chicken dumplings", "organic brown eggs", "vodka pasta sauce", "pasta", "spaghetti squash"]
bush_market = ["gochujang", "garlic bread", "vodka sauce", "red onion", "garlic"  ]
all_lists = {"amazon":amazon, "whole foods":whole_foods, "trader joes":trader_joes, "bush market":bush_market}

def select_from_menu():
	selection = int(raw_input("\nSelect one: \n0 - Main Menu \n1 - Show all lists \n2 - Show a specific list \n3 - Add a new shopping list \n4 - Add an item to a shopping list \n5 - Remove an item from a shopping list. \n6 - Remove a list by nickname. \n7 - Exit when you are done.\n"))
	return selection

def show_all_lists():
	return all_lists.items() 

def show_specific_list():
	print all_lists.keys()
	specific_list = raw_input("Which list would you like to print? ")
	if specific_list.lower() == 'amazon':
		return amazon
	elif specific_list.lower() == 'whole foods':
		return whole_foods
	elif specific_list.lower() == 'exitrader joes':
		return trader_joes
	elif specific_list.lower() == 'bush market':
		return bush_market
	else:
		return "That list does not exist."

def add_new_list():
	temp_list = [] 
	new_list_name = raw_input("What is the name of the new list? ")
	new_list_items = raw_input("Enter items to add to the list, separate with a comma ','.\n")
	temp_list += new_list_items.split(",")
	new_list_name = temp_list
	all_lists[new_list_name] = temp_list
	return new_list_name
 
def main ():
	while(True):
		selection=select_from_menu()
		if selection == 0: 
			print "Main Menu"
		elif selection == 1:
			print "Show all lists:", show_all_lists()
		elif selection == 2:
			print show_specific_list()
		elif selection == 3: 
			print "Add a new shopping list:", add_new_list()
		elif selection == 4: 
			print "Add an item to a shopping list"
		elif selection == 5:
			print "Remove an item from a shopping list."	
		elif selection == 6:
			print "Remove a list by nickname"
		elif selection == 7: 
			print "Goodbye"
			break
		else: 
			print "You're a disappointment." 

if __name__ == '__main__':
	main()
