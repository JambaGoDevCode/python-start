#   String Operations

message = "Hello Python"
print('Before uppercase:', message)

# Convert uppercase the elements in a string
menssage_upper = message.upper()
print('After uppercase:', menssage_upper)

# Convert lowercase the elements in a string
message_lower = message.lower()
print('After lowercase:', message_lower)

# Convert firt letter of string to ippercase
message_title = message.title()
print('The first element of the string is uppercase:', message_title)


# Replace() method in a string
messageH = 'Hello Python!'
message_hi = messageH.replace('Hello','Hi')
message_python = message.replace('Python','Javascript')
print(message_hi)
print(message_python)



# find method application in a string
# The output is the index number of the first element of the substring 
message = 'Começando a usar o python de um jeito mais avançado'
print(message.find('jeito'))


# find( method application to obtain a substring in a string)
# if cannot find the substring in a string, the output is -1
print(message.find('o'))


text = 'Jean-Paul Sartre somewhere observed that we each of us make our own hell out of the people around us.'

# find the first index of the substring 'Observed'
print(text.find('observed'))

# replace the subtring
print(text.replace('observed', 'visualization'))
print(text)
print(text.lower())

# convert the first letter of text to capital letter
print(text.capitalize())

# casefold() method returns a string where all the characters are in lower case
print(text.casefold())



# Center() method will center align the string, using a specified character (space is the default) as the fill character. 
messager = "Hello Jamba!"
print(messager.center(50,'-'))


# count() method returns the number of elements with the specified value
newText = 'jean-paul sartre somewhere observed that we each of us make our own hell out of the people around us. had jean-paul known nancy, he may have noted that at least one man, someday, might get very lucky, and make his own heaven out of one of the people around him. she will be his morning and his evening star, shining with the brightest and the softest light in his heaven. she will be the end of his wanderings, and their love will arouse the daffodils in the spring to follow the crocuses and precede the irises. their faith in one another will be deeper than time and their eternal spirit will be seamless once again.'

print(newText.count('and'))
print(newText.format(word ='and'))

# Format()  method

'''
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}.
'''

txt = "Hello {World}"
print(txt.format(World = "Capital"))

messageOne = 'Hi, My name is {} and i am {} years old'
print(messageOne.format('Jamba', 30))

messageOne = 'Hi, My name is {nome} and i am {idade} years old'
print(messageOne.format(nome='Jamba', idade=30))

messageOne = 'Hi, My name is {0} and i am {1} years old'
print(messageOne.format('Jamba', 30))