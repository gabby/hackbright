for x in range(1, 21):
	print x,  

for y in range(1,21):
	if y == 13:
		print "hello"
	print y,

fruits = ["apples, oranges", "bananas"]
for each in fruits:
	print each, 

for item in range(len(fruits)):
	print fruits


def sum_nums(z):
	my_list = range(0,z)
	total = 0
	for z in my_list:
		total = total + z
	print (total)

sum_nums(3)
sum_nums(6)

def sum_nums_plus(w):
	w == w + 1
	my_list = range(0, w)
	total = 0
	for w in my_list:
		total = total + w
	total = total + w
	print (total)

sum_nums_plus(3)
sum_nums_plus(6) 

def sum_nums2(g):
	my_list = range(g, 0)
	total = 0
	for g in my_list:
		total = total + g
	print (total)

sum_nums2(-7)
sum_nums2(-3)


def fizz_buzz():
	for num in range(1, 101):
		if (num % 3 == 0):
			print "Fizz",
		elif (num % 5 == 0):
			print "Buzz",
		elif (num % 3 == 0) and (num % 5 == 0):
			print "FizzBuzz",
		else: 
			print num,
fizz_buzz()