#1. Split each list item at the comma into 2 separate strings
#2. Split those 2 separate strings at the ':' 
#3. Set Odd index as the Key and the even index as the value, every other 

def convert_mene_to dict(menu_list): 
	menu = {}
	for i in menu_list:
		#1. split at the comma 
		pair = i.split(",")
		#2. split at the : 
		food = pair[0].split(':')[1] 
		#[1] is not related to pair[0] 
