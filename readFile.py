
file = open("dictionary.txt", "w", encoding = 'utf-8')
file.write("To write or not to write\nthat is the question!\n")
file.close()

file = open("dictionary.txt" , "a", encoding = "utf-8")
file.write("this is awesome\n")
file.write("yea")
file.close()

line_number = 0
with open("dictionary.txt", "r", encoding = "utf-8") as file:
	for line in file:
		line_number += 1
		print("{:>3}. {}".format(line_number, line.rstrip()))
	

