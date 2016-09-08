class Contact(object):
	def __init__ (self, first_name, last_name, mobile_phone="", home_phone="", twitter="", email="", home_address=""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_phone = mobile_phone
		self.home_phone = home_phone
		self.twitter = twitter
		self.email = email 
		self.home_address = home_address 


	def send_text(self, message):
		if self.mobile == "":
			print "A mobile phone number has not been saved for %s %s. Text message cannot be sent." % (self.first_name, self.last_name)
		else:
			print "To: %s - %s" % (self.mobile_phone, message)
