import contact_manager 

def contacts_menu(): 
	return """\nSelect one: \n0 - Main Menu \n1 - Show all contacts \n2 - Add a new contact  
	\n3 - Edit a contact \n4 - Delete a contact \n5 - Exit\n"""

def main():
	#while(True):
	print contacts_menu()
	if __name__ == '__main__':
		main()