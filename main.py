# Run Python programs
firstName = 'Melissa'
lastName = 'White'
print(firstName, lastName)
line1 = '"Row, row, row your boat\n'
line2 = 'Gently down the stream\n'
line3 = 'Merrily, merrily, merrily, merrily\n'
line4 = 'Life is but a dream"'
print(line1, line2, line3, line4)


# Variables
x = 4
y = 2
print(x, y, 3)
sum = 64 + 32
print(sum)
print(x + y)


# Strings
actor = "Brad Pitt"
print(actor)
s = "My lucky number is %d" % 49
print(s[3:8])
today = "Today is %d/%d/%d" % (3,15, 2021)
print(today)


# String replace
name = 'John'
greeting = 'Hello ' + name + '!'
print(greeting)
newGreeting = greeting.replace('John', 'Jim')
print(newGreeting)
  #Can a string be replaced twice? -Yes
newGreeting2 = greeting.replace('John', 'Mary')
print(newGreeting2)
  #Does replace only work with words or also phrases? -It also works with phrases
newGreeting3 = greeting.replace('Hello', 'Hello there')
print(newGreeting3)
newGreeting4 = newGreeting3.replace('Hello there', 'Good afternoon,')
print(newGreeting4)


# String find
  #Find out if string find is case sensitive -Yes, it is case sensitive
quote = "A dream is a wish your heart makes"
searchWord = quote.find("wish")
print(searchWord)
searchWord2 = quote.find("Wish")
print(searchWord2)
  #What if a query string appears twice in the string? -It finds the first occurrence
quote2 = "A dream is a wish wish your heart makes"
searchWord3 = quote.find("wish")
print(searchWord3)
  #Write a program that asks console input and searches
names = "Joe, Melissa, Bob, Mary"
name = input("Enter your name: ")
print(names.find(name))
print(name in names)

