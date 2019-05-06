from synthesizer import synthesize

import os, os.path

file_name = input("which file(s) would you like to read in?\n") # raven
size = int(input("how many characters should we look back?\n") ) # 8
num_chars = int(input("how many characters should we generate?\n") ) # 400

input_text = ""

if "," in file_name:
	file_names = file_name.replace(" ", "").split(",")
	for name in file_names:
		with open ("input/" + name + ".txt", "r") as file:
			input_data = file.readlines()
		input_text += "\n".join(input_data)
else:
	input_data = []
	with open ("input/" + file_name + ".txt", "r") as file:
		input_data = file.readlines()
	input_text = "\n".join(input_data)

output = synthesize(input_text, size, num_chars)
print(output)

# https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python
num_outputs = len([name for name in os.listdir("output")])

file = open("output/output-" + str(num_outputs) + ".txt", "w")
file.write(file_name + " - " + str(size) + " - " + str(num_chars) + "\n")
file.write(output)
file.close()

file = open("speaker/data.txt", "w")
file.write(output)
file.close()

input("Press Enter to continue...")
