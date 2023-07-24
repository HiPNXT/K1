user_input = int(input("Nhap 1 so: "))

with open("data.txt", "w") as f:
	for i in range(user_input):
		f.write(str(user_input - i) + "\n")

numbers = []
with open("data.txt", "r") as f:
	numbers = f.read().split()


for i in range(len(numbers)):
	print("Line " + str(i+1) +": "+str(numbers[i]))