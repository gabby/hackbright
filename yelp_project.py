#documentation: https://github.com/Yelp/yelp-python
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
    'location': 'Argentina',
    'limit': 19
}

response = client.search(**params)

#print response
#print response.businesses[18].name, response.businesses[18].location.display_address, response.businesses[18].display_phone
print response.businesses
#print response.businesses[0].location.display_address

#location, count, search_term=""
# def print_biz_info():
# 	for entry in response.businesses:
# 		print response.businesses[entry].name
# 		print response.businesses[entry].location.display_address
# 		print response.businesses[entry].display_phone

# def main():
# 	print print_biz_info()

# if __name__ == '__main__':
# 	main()
# for address in 
# # #print pprint(dir(response))

#  1. Get input for Location, Count, search_term
#  2. Append params dictionary with Key and values matching Yelp APi documentation and raw inputs 
#  3. reassign that params  dictionary for the `response` variable 




