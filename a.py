import datetime
def ask_yes_no(promopt):
	answer_list = ["yes", "y", "Y"]
	answer_list2 = ["no", "n", "N"]
	i = 0
	while True:
		answer = input(promopt)
		if answer in answer_list:
			return True
		elif answer in answer_list2:
			return False
		else:
			i = i + 1
			print("Ban da nhap " + str(i) + " lan")
			print("\n")
			print("Please input again ", end = "")

def cal_age(year_born):
	now = datetime.datetime.now()	
	CURRENT_YEAR = now.year
	return CURRENT_YEAR - year_born

def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.281
	return round(meter * METER_TO_FEET ,1)

def print_height(height, male, name):
	if male:
		if height > 6.5:
			print(name + " is", end = " ")
			for i in range(3):
				print("very ", end = "")
			print('tall as a man with ' + str(height_feet) + " feet")
		elif height > 6.0:
			print("{0} is tall as a man with {1} feet". format(name,height))
	elif male is False:
		if height > 6.0:
			print("{0} are very tall as a girl with {1} feet". format(name,height))
		elif height >= 5.7:
			print("{0} is very tall as a girl with {1}". format(name,height))
	else:
		print("Syntax error: please check your 'input'")

def print_info(name, age, height_feet, is_male):
	now = datetime.datetime.now()	
	CURRENT_YEAR = now.year
	print("Your height (feet): " + str(height_feet))
	print("{0} are {1} years old in {2}". format(name, age, CURRENT_YEAR))
	print_height(height_feet, is_male, name)

def ask_info():
	name = input("Your name: ")
	year_born = int(input("Your born: "))
	height_meter = float(input("Your height (meter): "))
	is_male = ask_yes_no("Are you male (yes/no): ")
	return name, year_born, height_meter, is_male

def main():
	name, year_born, height_meter, is_male = ask_info()
	print("\n ------------------ \n")
	age = cal_age(year_born)
	height_feet = convert_meter_to_feet(height_meter)
	print_info(name, age, height_feet, is_male)	

main()