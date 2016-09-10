
import json
from pprint import pprint 
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

all_data_results=[]
# read API keys
with open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

params = {
 	"limit": 20,
}   
#print response
#print response.businesses[18].name, response.businesses[18].location.display_address, response.businesses[18].display_phone
#print response.businesses
#print response.businesses[0].location.display_address

#location, count, search_term=""
designated_location = raw_input("From where address? ")

response = client.search(designated_location, term="nail salon", **params)
print params 
print response.businesses[18].name, response.businesses[18].location.display_address, response.businesses[18].display_phone



# def biz_info(num):
# 	for entry in range(num):
# 		print response.businesses[entry].name, response.businesses[entry].display_phone
# 		print response.businesses[entry].location.display_address, "\n"

# def main():
# 	search_term = raw_input("Where do you want these addresses from: ")
# 	print add_params(search_term)
# 	num_entries = int(raw_input("How many entries do you need? "))
# 	print "\n"
# 	print biz_info(num_entries)


# if __name__ == '__main__':
# 	main() 
 
# # #print pprint(dir(response))

#  1. Get input for Location, Count, search_term
#  2. Append params dictionary with Key and values matching Yelp APi documentation and raw inputs 
#  3. reassign that params  dictionary for the `response` variable 



	# for info in all_contacts:
	# 		if info.first_name == fname and info.last_name == lname:
	# 			print(info.first_name, info.last_name, info.mobile_phone, info.home_p

#there is a note in here 
