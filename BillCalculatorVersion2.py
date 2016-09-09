tip_amount = 0
total_bill = 0
split_amount = 0

def calculate_bill(original_bill_amount, tip_percentage = 18, split_number = 1): 
	global total_bill, split_amount
	total_bill = original_bill_amount * tip_percentage * .01 + original_bill_amount
	split_amount = total_bill / split_number
	return total_bill, split_amount

	print "tip amount %i.0" % float(tip_amount)
	print "total bill %r" % float(total_bill)
	print "split amount %r" % float(split_amount)

print calculate_bill(100)
print calculate_bill(100, tip_percentage = 20)
print calculate_bill(100, tip_percentage = 25, split_number = 3)
print calculate_bill(100, split_number = 2)
