#import all_lists.txt 

amazon = ["deodorant", "dish soap", "hand soap", "toilet paper"]
whole_foods = ["salmon filets", "cantaloupe", "black grapes", "zucchini"]
trader_joes = ["chicken dumplings", "organic brown eggs", "vodka pasta sauce", "pasta", "spaghetti squash"]
bush_market = ["gochujang", "garlic bread", "vodka sauce", "red onion", "garlic"  ]
all_lists = {"amazon":amazon, "whole foods":whole_foods, "trader joes":trader_joes, "bush market":bush_market}

def select_from_menu():
	return """\nSelect one: \n0 - Main Menu \n1 - Show all lists \n2 - Show a specific list \n3 - Add a new shopping list \n4 - Add an item to a shopping list \n5 - Remove an item from a shopping list.\n6 - Remove a list by nickname. \n7 - Exit when you are done.\n"""

def show_all_lists():
	return all_lists.items() 

def show_specific_list(specific_list):
	if specific_list.lower() == 'amazon':
		return amazon
	elif specific_list.lower() == 'whole foods':
		return whole_foods
	elif specific_list.lower() == 'trader joes':
		return trader_joes
	elif specific_list.lower() == 'bush market':
		return bush_market
	else:
		return "That list does not exist."

def add_new_list(thing1, thing2):
	temp_list = [] 
	temp_list += thing2.split(",")
	all_lists[thing1.lower()] = temp_list
	return thing1.lower(), temp_list

def add_item(list_to_add, item_added): 
	check_items = all_lists[list_to_add.lower()]
	if item_added.lower() in check_items:
		print "This item is already in the `%s` list and does not need to be added." % (list_to_add.lower()) 
	else:
		all_lists[list_to_add.lower()].append(item_added)
		print "`%s` has been added to the `%s` list." % (item_added, list_to_add.lower())
	return list_to_add.lower(), all_lists[list_to_add.lower()]

def remove_item(list_to_remove, item_removed):
	check_items = all_lists[list_to_remove.lower()]
	if item_removed.lower() not in check_items:
		print "'%s' is not currently an item in the '%s' list and cannot be removed." % (item_removed.lower(), list_to_remove.lower())
	else:
		all_lists[list_to_remove.lower()].remove(item_removed.lower())
		print "`%s' has been removed from the `%s' list." % (item_removed.lower(), list_to_remove.lower())
	return list_to_remove.lower(), all_lists[list_to_remove.lower()]

def remove_list(delete_list_selection):
	del all_lists[delete_list_selection.lower()]
	return all_lists.items() 

#def write_to_lists(file_name):
	#with open (file_name, mode="a") as my_file: 



 
def main ():
	while(True):
		print select_from_menu()
		selection = int(raw_input("Please select from the menu. "))
		if selection == 0: 
			print "Main Menu\n"
		elif selection == 1:
			print "Show all lists:\n", show_all_lists()
			print "----------------------"
		elif selection == 2:
			print all_lists.keys()
			specific_list = raw_input("Which list would you like to print?\n")
			if specific_list.lower() in all_lists:
				print show_specific_list(specific_list)
				print "----------------------"
			else: 
				print "The `%s` list does not exist. To create a list, select option 3." % (specific_list)
				print "----------------------"
		elif selection == 3: 
			new_list_name = raw_input("What is the name of the new list? ")
			if new_list_name.lower() in all_lists:
				print "The '%s' list already exists.\n" % (new_list_name), new_list_name, all_lists[new_list_name] 
				print "To add new items to this list, select option 4."
				print "----------------------"
			else:
				new_list_items = raw_input("Enter items to add to the list, separate with a comma ','.\n")
				print add_new_list(new_list_name, new_list_items)
				print "----------------------"
		elif selection == 4: 
			print all_lists.keys()
			add_selection = raw_input("What list do you want to add to? ")
			if add_selection.lower() in all_lists:
				item_to_add = raw_input("What item do you want to add? ")
				print "Add an item to a shopping list.\n", add_item(add_selection, item_to_add)
				print "----------------------"
			else:
				print "The '%s' list does not exist. To create a list, select option 3." % (add_selection)
				print "----------------------"
		elif selection == 5:
			print all_lists.keys()
			remove_selection = raw_input("What list do you want to remove from? ")
			if remove_selection.lower() in all_lists:
				item_to_remove = raw_input("What item do you want to remove? ")
				print "Remove an item from a shopping list.\n", remove_item(remove_selection, item_to_remove)
				print "----------------------"
			else:
				print "The '%s' list does not exist. No items to remove." % (remove_selection)
				print "----------------------"
		elif selection == 6:
			print all_lists.keys()
			delete_list = str(raw_input("What list do you want to remove?\n"))
			if delete_list.lower() in all_lists: 
				print delete_list.lower(), all_lists[delete_list.lower()]
				confirm_delete = raw_input("Please confirm to delete list: Y/N ")
				if confirm_delete.lower() == 'y' or confirm_delete.lower() == 'yes':
					print remove_list(delete_list), "Ok. The `%s` list has been deleted." % (delete_list)
					print "----------------------"
				else:
					print "Ok. List has not been deleted."
					print "----------------------"
				main() 
			else:
				print "The '%s' list does not exist. Nothing to remove." % (delete_list)
				print "----------------------"
				main() 

		elif selection == 7: 
			print "Goodbye"
			print "----------------------"
			break
		else: 
			print "You're a disappointment. Please select an option available in the menu."
			print "----------------------"
			main()

if __name__ == '__main__':
	main()
