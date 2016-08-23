def sum_nums(num):
	count = 0 
	while (count < num): 
		num = num + count
		count += count + 1
		print num 

sum_nums(4) 

