def hello_world(name,point):
	print("Name: " + name)
	print("Math: " + str(point))
	if point>5:
		print("Good!")
	else:
		print("Bad")

def main():
	number_student = int(input("How many student? "))
	j = 1
	for alpha in "ABCDEFGH":
		if j>number_student:
			break
		print("Student: " + alpha)
		student_name = input("Student name: ")
		point_test = float(input("Student point: "))
		hello_world(student_name,point_test)
		j += 1
		print("\n ---------- \n")
main()