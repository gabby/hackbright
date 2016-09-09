grocery_list = []

def add_item():
	add_item = raw_input("What item do you want to add? ")
	add_item = add_item.lower()
	if add_item in grocery_list:
		print "Item is already on the list."
		grocery_list.sort()
		print grocery_list
		main()
	elif add_item not in grocery_list:
		grocery_list.append(add_item)
		grocery_list.sort()
		print grocery_list
		main()

def remove_item():
	remove_item = raw_input("What item do you want to remove? ")
	remove_item = remove_item.lower()
	if remove_item not in grocery_list:
		print "This item cannot be removed because it was not on the list."
		main()
	elif remove_item in grocery_list:
		grocery_list.remove(remove_item)
		print grocery_list
		main()

def main():
	action = int(raw_input("\nChoose:\n1 - Add item 2 - Remove item 3 - Grocery List\n"))
	if action == 1:
		add_item()
	elif action == 2:
		remove_item()
	elif action == 3: 
		grocery_list.sort()
		print "Here is your grocery list: ", grocery_list


if __name__ == '__main__':
	main() 

#Input item, append if unique, nothing if duplicate, remove if available, nothing if it does not exist
#when user writes done, print 


