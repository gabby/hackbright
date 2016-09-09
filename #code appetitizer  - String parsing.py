#code appetitizer  - String parsing
###  if we pass it thru a range() we'll get an index back 

def convert_tuple_to_dictionary():
	food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99) 
	food_price_dict = {}
	food_item = 'sushi'
	for menu_item in range(len(food_price_tuple)):
		if menu_item % 2 --0:
			food_item = food_price_tuple[menu_item]
		else:
			food_price_dict[food_item] = food_price_tuple[menu_item]
		return food_price_dict

print convert_tuple_to_dictionary()