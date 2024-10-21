# open the file
# read file

with open("snowwhite.txt", 'r') as file:
    content = file.read()

lines = content.split(". ")
correct_sent = []

for line in lines:
    line = line.capitalize()
    correct_sent.append(line)

new_line = ". ".join(correct_sent)

# process file
with open("snowwhite_corrected.txt", "w") as file:
    file.write(new_line)

