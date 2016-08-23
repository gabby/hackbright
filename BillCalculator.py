def tip_amount(amount, percent):
	tip_total = amount * percent * .01
	return tip_total

def final_bill(amount, percent):
	tip_total = tip_amount(amount, percent)
	final = tip_total + amount
	return final

def split_bill(guests, bill):
	split = bill / guests
	return split 

def main(): 
	menu_choice = int(raw_input("Please choose: \n1 - calculate tip \n2 - split the bill \n"))
	if menu_choice == 1:
		bill = float(raw_input("How much was the original bill? $"))
		percent = int(raw_input("What percent would you like to tip? "))
		print round(tip_amount(bill, percent), 2)
		print round(final_bill(bill, percent), 2)
		split_request = raw_input("Would you like to split the bill? Y/N ")

		if split_request == "Y":
			guests = int(raw_input("How many ways would you like to split? "))
			print round(split_bill(guests, final_bill(bill, percent)), 2) 
		else: 
			print "Ok, have a nice day!"

	elif menu_choice ==2: 
		total_bill = float(raw_input("What was the total bill amount? $"))
		guests = int(raw_input("How many ways would you like to split? "))
		print round(split_bill(guests, total_bill), 2)


if __name__ == '__main__':
	main()
