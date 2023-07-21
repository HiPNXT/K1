print("hieu")

you = input()

if you == "":
	robot_brain = "I can't hear you"
elif you == "Hello":
	robot_brain = "Hello PNXT"
elif you == "Today":
	robot_brain = "Thu 4"
else :
	robot_brain = "Say again!"

print(robot_brain)