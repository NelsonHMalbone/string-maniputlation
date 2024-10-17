# getting the content from the file
with open('example.txt') as file:
    # 'r' flag is default so for simplicity just be as above
    content = file.read()


words = content.split() # placing words into a list

# creating a new list for reverse words
reverse_words = []
for word in words:
    word = word[::-1]
    # using the start stop step
    reverse_words.append(word)

# create a method to process new word into a file

# coverting reverse_word to a str
reverse_text = " ".join(reverse_words)

with open("reversed_words.txt", 'w') as file:
    # can use same 'file' as the read section due to it being a enclosed
    # content manager
    file.write(reverse_text)