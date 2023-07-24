from random import randint

print("MOI BAN CHON")
player = input()

print("-----------")
computer = randint(0,2)

if computer == 0:
	computer = "Bua"

elif computer == 1:
	computer = "Keo"

else:
	computer = "Bao"

print("Ban chon: " + player)
print("May chon: " + computer)

if computer == player:
	print("Draw")

else:
	if player == "Bua":
		if computer == "Keo":
			print("You Win")
		else:
			print("You Lose")

	elif player == "Keo":
		if computer == "Bao":
			print("You Win")
		else:
			print("You Lose")

	else:
		if computer == "Bua":
			print("You Win")
		else:
			print("You Lose")