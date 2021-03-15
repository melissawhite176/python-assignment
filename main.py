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
mySum = 64 + 32
print(mySum)
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
  #What if a query string appears twice in the string? -It finds the first occurrence unless you use position
quote2 = "A dream is a wish wish your heart makes"
searchWord3 = quote2.find("wish")
print(searchWord3)
searchWord4 = quote2.find("wish", 18, 25)
print(searchWord4)
  #Write a program that asks console input and searches
names = "Joe, Melissa, Bob, Mary"
name = input("Enter your name: ")
print(names.find(name))
print(name in names)

# String join
listNames = ['Joe', 'Melissa', 'Bob', 'Mary']
sep = ', '
joinNamesSpace = sep.join(listNames)
print(joinNamesSpace)
sep = '_'
joinNamesUnderscore = joinNamesSpace.replace(", ", "_")
print(joinNamesUnderscore)

firstName = "Harry"
lastName = "Potter"
sequence = (lastName, firstName)
fullName = ", ".join(sequence)
print(fullName)

# String split
  #Can a string be split on multiple characters? -Yes
quote = "A dream is a wish your heart makes"
splitQuote = quote.split('ea')
print(splitQuote)
  #Can you split a string this string?: World,Earth,America,Canada
places = "World,Earth,America,Canada"
splitPlaces = places.split(",")
print(splitPlaces)
  #Given an article, can you split it based on phrases?
speech = "I have a dream that one day this nation will rise up and live out the true meaning of its creed, We hold these truths to be self-evident, that all men are created equal. I have a dream that one day on the red hills of Georgia, sons of former slaves and the sons of former slaveowners will be able to sit down together at the table of brotherhood. I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice."
splitSpeech = speech.split("I have a dream")
print(splitSpeech)

# Random numbers
  #Make a program that creates a random number and stores it into x.
import random
print(random.randint(1, 100))
  #Make a program that prints 3 random numbers.
count = 1
while count < 4:
  randomInt = random.randint(1, 100)
  print("random number %d:" % count, randomInt)
  count += 1
  #or
randomNums = [random.randint(1, 100) for x in range(3)]
print(randomNums)
  #Create a program that generates 100 random numbers and find the frequency of each number.
randomNums = [random.randint(1, 100) for x in range(100)]
print(randomNums)

import collections
print("Count Frequency of Numbers: ")
countNums = collections.Counter(randomNums)
print(countNums)

# Keyboard input
phone = input("Please enter your phone number: ")
print(phone)
favLanguage = input("What's your favorite programming language?: ")
print(favLanguage)

#If statements
numLimit = range(1, 11)
pickNum = input("Please choose a number between 1 to 10: ")
print(type(pickNum))
if len(pickNum) == 0:
  print("no input provided")
else:
  pickNum = int(pickNum)
  if pickNum not in numLimit:
    print("invalid number")

  #program that asks for a password
import getpass 
print("Please enter a password between 10-15 characters")
password = getpass.getpass() 

print('Password entered:', password) 
print(len(password))
min = 10
max = 15
length = len(password)
if (length < 10) or (length > 15):
  print("Password must be between 10-15 characters. Try again.")



# For loops
clist = ["Canada","USA","Mexico"]
i = 0
while (i < len(clist)):
  print(clist[i])
  i += 1

  # 2. Both are control flow statements. While loops executes the code block once and continue to execute as long as a condition is true. Number of iterations is unknown. For loops execute and repeat a code block when a condition is true until a specified condition is met.
for item in clist:
  print("Place: " + item)

  #Can you sum numbers in a while loop? -Yes

x = 1
while (x < 5):
  add1 = x + 1
  print("x + 1 is equal to: %d "% add1)
  x += 1

#Can a for loop be used inside a while loop? -Yes
whileCount = 0
while (whileCount < 3):
  numList = [2, 4, 6]
  for item in numList:
    product = whileCount * item
    print(product)
  whileCount += 1

#Functions
mylist = [1, 2, 3, 4, 5]
def sumList():
  total = sum(mylist)
  print("mylist sum: ", total)
# sumList()

myFloats = [1.22, 2.52, 3.18, 4.32, 5.86]
def toInts():
  i = 0
  for item in myFloats:
    myFloats[i] = int(myFloats[i])
    i += 1
  print("myFloats to integers: ", myFloats)  
# toInts()

def funcsInFunc():
  sumList()
  toInts()

print("Calling functions inside a function: ")
funcsInFunc()

print("Recursive Function- Function that calls itself")
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))     
num = 3
print("Factorial of", num, "is", factorial(num))

print("Scope- Can variables defined in a function be used in another function?")