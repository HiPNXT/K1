class Student:
	def __init__(self):
		self.name = None
		self.age = None
		self.math_score = None
		self.lit_score = None
		self.teacher = None

	def average_score(self):
		return (self.math_score + self.lit_score)/2

	def print_info(self):
		ave = str(self.average_score())
		print("Student name " + self.name + " study with " + self.teacher + " have average score " + ave)

students = []
s1 = Student()
nhap_so_lan = int(input("Nhap so hoc sinh: "))
for i in range(nhap_so_lan):
	s1.name = input("Nhap ten hoc sinh thu " + str(i+1) + ":  ")
	s1.age = int(input("Nhap so tuoi: "))
	s1.math_score = float(input("Nhap diem toan: "))
	s1.lit_score = float(input("Nhap diem van: "))
	s1.teacher = input("Nhap ten gv: ")
	students.append(s1)
	# s1.print_info()
	# print("\n ---------------- \n")

for i in range(len(students)):
	students[i].print_info()