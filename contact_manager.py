from contacts import Contact

all_contacts = []
	

def show_all_contacts():
	for info in all_contacts:
		return (info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)

def add_new_contact(fname, lname):
	if all_contacts == []:
		print "Enter additional info for contact '%s %s' To skip entry, press return." % (fname, lname)
		mobile = raw_input("Mobile number: ")
		home = raw_input("Home number: ")
		tweet = raw_input("Twitter handle: ")
		email_addy = raw_input("Email address: ")
		addy = raw_input("Home address: ")
		new_entry = Contact(fname, lname, mobile, home, tweet, email_addy, addy) 
		return all_contacts.append(new_entry)
	else:
		for entry in all_contacts:
			if entry.first_name == fname and entry.last_name == lname:
				return "A contact matching the first and last name already exists.", (entry.first_name, entry.last_name, entry.mobile_phone, entry.home_phone, entry.twitter, entry.email, entry.address)
			else: 
				print "Enter additional info for contact '%s %s' To skip entry, press return." % (fname, lname)
				mobile = raw_input("Mobile number: ")
				home = raw_input("Home number: ")
				tweet = raw_input("Twitter handle: ")
				email_addy = raw_input("Email address: ")
				addy = raw_input("Home address: ")
				new_entry = Contact(fname, lname, mobile, home, tweet, email_addy, addy) 
				return all_contacts.append(new_entry)

def edit_contact(fname, lname):
	if all_contacts == []:
		return """\nThe current contact list is empty.\nThere is no contact entry for '%s %s' to edit.\nTo add this contact, select option 1 from the menu.\n""" % (fname, lname)
	else:
		for info in all_contacts:
			if info.first_name == fname and info.last_name == lname:
				print(info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)
				print """ 1 - First name,\n 2 - Last name,\n 3 - Mobile number,\n 4 - Home Number\n 5 - Twitter handle\n 6 - Email address\n 7 - Home Address\n"""
				edit_attribute = int(raw_input("Select an attribute from the menu above. "))
				if edit_attribute == 1:
					new_fname = raw_input("New first name: ")
					info.first_name = new_fname
					return (info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)
				elif edit_attribute == 2:
					new_lname = raw_input("New last name: ")
					info.last_name = new_lname
					return (info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)
				elif edit_attribute == 3:
					new_mobile = raw_input("New mobile number: ")
					info.mobile_phone = new_mobile
					return (info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)
				elif edit_attribute == 4:
					new_home = raw_input("New home number: ")
					info.home_phone = new_home
					return (info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)
				elif edit_attribute == 5:
					new_twitter = raw_input("New Twitter handle: ")
					info.twitter = new_twitter
					return (info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)
				elif edit_attribute == 6:
					new_email = raw_input("New email address: ")
					info.email = new_email
					return (info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)
				elif edit_attribute == 7: 
					new_addy = raw_input("New home address: ")
					info.home_address = new_addy
					return (info.first_name, info.last_name, info.mobile_phone, info.home_phone, info.twitter, info.email, info.home_address)
				else:
					return "%i was not an option." % edit_attribute

				
#def delet#e_contact 
#ask user to get their ie fname, lname, and etc.. save input to variables 
# user_contact = Contact(fname, lname...)
#put that info to a file, comma delimiter 

def main():
	print add_new_contact("Gabby", "Sin")
	print edit_contact("Gabby", "Sin")


if __name__ == '__main__':
	main()
