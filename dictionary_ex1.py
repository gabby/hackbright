## NUMBER 2###
# def count_letters_in_name(name):
# 	letters_occurence = {} 
# 	name = name.lower()
# 	for i in name:
# 		if i not in letters_occurence:
# 			letters_occurence[i] = 1
# 		else:
# 			letters_occurence[i] += 1
# 	return letters_occurence

# count_letters_in_name("gabrielle") 

## NUMBER 3##
# prices = {"banana": 4, "apple":2, "orange":1.5, "pear":3}

# def most_exp(dict_name): 
# 	track_value = 0 
# 	track_key = None 
# 	for key, value in dict_name.items():
# 		if value > track_value:
# 			track_value = value
# 			track_key = key 
# 	return track_key 

# print most_exp(prices)

employee = {"name": "Gabrielle", "age":29, "height": None} 
height_input = int(raw_input("What is your height in inches? "))
employee["height"] = height_input 
print employee
# employee["age"] = 30
# print employee

# if 'name' in employee.keys():
# 	print "name", employee["name"]
# ## Why don't we use / can't we use: 
# 	# for key, value in employee.item(): 
# else:
# 	print "This key does not exist." 

if 26 in employee:
	## Why don't we use employee.keys(): here? we can just use employee?? 
	print 26, employee[26]
else:
	print 26 

for key in employee:
	#employee.items() ?? 
	print key 

print employee.keys()

for key, value in employee.items():
	print key, value 

print employee.items()