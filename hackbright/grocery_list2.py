grocery_list = []

def main():
	action = raw_input("?> ")
	action = action.lower()
	if action == 'add':
		add_item = raw_input("A> ")
		if add_item in grocery_list:
			main()
		elif add_item not in grocery_list:
			grocery_list.append(add_item)
			main() 
	elif action == 'remove':
		remove_item = raw_input("R> ")
		remove_item = remove_item.lower()
		if remove_item not in grocery_list:
			main()
		elif remove_item in grocery_list:
			grocery_list.remove(remove_item)
			main()			
	elif action == 'done':
		grocery_list.sort()
		print grocery_list 

if __name__ == '__main__':
	main()