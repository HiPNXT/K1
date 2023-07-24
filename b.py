with open("data.txt", "w") as f:
	f.write("pnxt\n")
	f.write("abc")
	f.write("zzz")

with open("data.txt", "w") as file:
	file.write("aazgsdfg\n")

with open("data.txt", "a") as file: 
	file.write("zzz")

with open("data.txt", "r") as f:
	data = f.read()
	print(data)