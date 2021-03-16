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

# Scope- Can variables defined in a function be used in another function? -no

def varInFunc():
  balance = 100
  print(balance - 50)

#cannot print this due to scope
# print(balance) 
# print(varInFunc().balance)



# Lists
states = ["Alaska","Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio","Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

print("all states")
for state in states:
  print(state)

print("states that start with M")
for state in states:
  if state.startswith("M"):
    print(state)




# List Operations
y = [6, 4, 2]
print('y:', y)
y.append(12)
y.append(8)
y.append(4)
print('y:', y)
y[1] = 3
print('y:', y)





#Sorting list
x = [(3,6), (4,7), (5,9), (8,4), (3,1)]
x.sort()
print('simple sort:', x)

import operator
x = [(3,6), (4,7), (5,9), (8,4), (3,1)]
x.sort(key = operator.itemgetter(0))
print('sort on first element:', x)
x.sort(key = operator.itemgetter(1))
print('now sorted on second element:', x)



# Range Function
thousand = list(range(1, 1001, 1))
print('max:', max(thousand))
print('min:', min(thousand))

evens = list(range(2, 11, 2))
print('even list:', evens)
odds = list(range(1, 10 , 2))
print('odd list:', odds)






# Dictionary
countriesDict = {
	'AD': 'Andorra',
	'AE': 'United Arab Emirates',
	'AF': 'Afghanistan',
	'AG': 'Antigua & Barbuda',
	'AI': 'Anguilla',
	'AL': 'Albania',
	'AM': 'Armenia',
	'AN': 'Netherlands Antilles',
	'AO': 'Angola',
	'AQ': 'Antarctica',
	'AR': 'Argentina',
	'AS': 'American Samoa',
	'AT': 'Austria',
	'AU': 'Australia',
	'AW': 'Aruba',
	'AZ': 'Azerbaijan',
	'BA': 'Bosnia and Herzegovina',
	'BB': 'Barbados',
	'BD': 'Bangladesh',
	'BE': 'Belgium',
	'BF': 'Burkina Faso',
	'BG': 'Bulgaria',
	'BH': 'Bahrain',
	'BI': 'Burundi',
	'BJ': 'Benin',
	'BM': 'Bermuda',
	'BN': 'Brunei Darussalam',
	'BO': 'Bolivia',
	'BR': 'Brazil',
	'BS': 'Bahama',
	'BT': 'Bhutan',
	'BU': 'Burma (no longer exists)',
	'BV': 'Bouvet Island',
	'BW': 'Botswana',
	'BY': 'Belarus',
	'BZ': 'Belize',
	'CA': 'Canada',
	'CC': 'Cocos (Keeling) Islands',
	'CF': 'Central African Republic',
	'CG': 'Congo',
	'CH': 'Switzerland',
	'CI': 'Côte D\'ivoire (Ivory Coast)',
	'CK': 'Cook Iislands',
	'CL': 'Chile',
	'CM': 'Cameroon',
	'CN': 'China',
	'CO': 'Colombia',
	'CR': 'Costa Rica',
	'CS': 'Czechoslovakia (no longer exists)',
	'CU': 'Cuba',
	'CV': 'Cape Verde',
	'CX': 'Christmas Island',
	'CY': 'Cyprus',
	'CZ': 'Czech Republic',
	'DD': 'German Democratic Republic (no longer exists)',
	'DE': 'Germany',
	'DJ': 'Djibouti',
	'DK': 'Denmark',
	'DM': 'Dominica',
	'DO': 'Dominican Republic',
	'DZ': 'Algeria',
	'EC': 'Ecuador',
	'EE': 'Estonia',
	'EG': 'Egypt',
	'EH': 'Western Sahara',
	'ER': 'Eritrea',
	'ES': 'Spain',
	'ET': 'Ethiopia',
	'FI': 'Finland',
	'FJ': 'Fiji',
	'FK': 'Falkland Islands (Malvinas)',
	'FM': 'Micronesia',
	'FO': 'Faroe Islands',
	'FR': 'France',
	'FX': 'France, Metropolitan',
	'GA': 'Gabon',
	'GB': 'United Kingdom (Great Britain)',
	'GD': 'Grenada',
	'GE': 'Georgia',
	'GF': 'French Guiana',
	'GH': 'Ghana',
	'GI': 'Gibraltar',
	'GL': 'Greenland',
	'GM': 'Gambia',
	'GN': 'Guinea',
	'GP': 'Guadeloupe',
	'GQ': 'Equatorial Guinea',
	'GR': 'Greece',
	'GS': 'South Georgia and the South Sandwich Islands',
	'GT': 'Guatemala',
	'GU': 'Guam',
	'GW': 'Guinea-Bissau',
	'GY': 'Guyana',
	'HK': 'Hong Kong',
	'HM': 'Heard & McDonald Islands',
	'HN': 'Honduras',
	'HR': 'Croatia',
	'HT': 'Haiti',
	'HU': 'Hungary',
	'ID': 'Indonesia',
	'IE': 'Ireland',
	'IL': 'Israel',
	'IN': 'India',
	'IO': 'British Indian Ocean Territory',
	'IQ': 'Iraq',
	'IR': 'Islamic Republic of Iran',
	'IS': 'Iceland',
	'IT': 'Italy',
	'JM': 'Jamaica',
	'JO': 'Jordan',
	'JP': 'Japan',
	'KE': 'Kenya',
	'KG': 'Kyrgyzstan',
	'KH': 'Cambodia',
	'KI': 'Kiribati',
	'KM': 'Comoros',
	'KN': 'St. Kitts and Nevis',
	'KP': 'Korea, Democratic People\'s Republic of',
	'KR': 'Korea, Republic of',
	'KW': 'Kuwait',
	'KY': 'Cayman Islands',
	'KZ': 'Kazakhstan',
	'LA': 'Lao People\'s Democratic Republic',
	'LB': 'Lebanon',
	'LC': 'Saint Lucia',
	'LI': 'Liechtenstein',
	'LK': 'Sri Lanka',
	'LR': 'Liberia',
	'LS': 'Lesotho',
	'LT': 'Lithuania',
	'LU': 'Luxembourg',
	'LV': 'Latvia',
	'LY': 'Libyan Arab Jamahiriya',
	'MA': 'Morocco',
	'MC': 'Monaco',
	'MD': 'Moldova, Republic of',
	'MG': 'Madagascar',
	'MH': 'Marshall Islands',
	'ML': 'Mali',
	'MN': 'Mongolia',
	'MM': 'Myanmar',
	'MO': 'Macau',
	'MP': 'Northern Mariana Islands',
	'MQ': 'Martinique',
	'MR': 'Mauritania',
	'MS': 'Monserrat',
	'MT': 'Malta',
	'MU': 'Mauritius',
	'MV': 'Maldives',
	'MW': 'Malawi',
	'MX': 'Mexico',
	'MY': 'Malaysia',
	'MZ': 'Mozambique',
	'NA': 'Namibia',
	'NC': 'New Caledonia',
	'NE': 'Niger',
	'NF': 'Norfolk Island',
	'NG': 'Nigeria',
	'NI': 'Nicaragua',
	'NL': 'Netherlands',
	'NO': 'Norway',
	'NP': 'Nepal',
	'NR': 'Nauru',
	'NT': 'Neutral Zone (no longer exists)',
	'NU': 'Niue',
	'NZ': 'New Zealand',
	'OM': 'Oman',
	'PA': 'Panama',
	'PE': 'Peru',
	'PF': 'French Polynesia',
	'PG': 'Papua New Guinea',
	'PH': 'Philippines',
	'PK': 'Pakistan',
	'PL': 'Poland',
	'PM': 'St. Pierre & Miquelon',
	'PN': 'Pitcairn',
	'PR': 'Puerto Rico',
	'PT': 'Portugal',
	'PW': 'Palau',
	'PY': 'Paraguay',
	'QA': 'Qatar',
	'RE': 'Réunion',
	'RO': 'Romania',
	'RU': 'Russian Federation',
	'RW': 'Rwanda',
	'SA': 'Saudi Arabia',
	'SB': 'Solomon Islands',
	'SC': 'Seychelles',
	'SD': 'Sudan',
	'SE': 'Sweden',
	'SG': 'Singapore',
	'SH': 'St. Helena',
	'SI': 'Slovenia',
	'SJ': 'Svalbard & Jan Mayen Islands',
	'SK': 'Slovakia',
	'SL': 'Sierra Leone',
	'SM': 'San Marino',
	'SN': 'Senegal',
	'SO': 'Somalia',
	'SR': 'Suriname',
	'ST': 'Sao Tome & Principe',
	'SU': 'Union of Soviet Socialist Republics (no longer exists)',
	'SV': 'El Salvador',
	'SY': 'Syrian Arab Republic',
	'SZ': 'Swaziland',
	'TC': 'Turks & Caicos Islands',
	'TD': 'Chad',
	'TF': 'French Southern Territories',
	'TG': 'Togo',
	'TH': 'Thailand',
	'TJ': 'Tajikistan',
	'TK': 'Tokelau',
	'TM': 'Turkmenistan',
	'TN': 'Tunisia',
	'TO': 'Tonga',
	'TP': 'East Timor',
	'TR': 'Turkey',
	'TT': 'Trinidad & Tobago',
	'TV': 'Tuvalu',
	'TW': 'Taiwan, Province of China',
	'TZ': 'Tanzania, United Republic of',
	'UA': 'Ukraine',
	'UG': 'Uganda',
	'UM': 'United States Minor Outlying Islands',
	'US': 'United States of America',
	'UY': 'Uruguay',
	'UZ': 'Uzbekistan',
	'VA': 'Vatican City State (Holy See)',
	'VC': 'St. Vincent & the Grenadines',
	'VE': 'Venezuela',
	'VG': 'British Virgin Islands',
	'VI': 'United States Virgin Islands',
	'VN': 'Viet Nam',
	'VU': 'Vanuatu',
	'WF': 'Wallis & Futuna Islands',
	'WS': 'Samoa',
	'YD': 'Democratic Yemen (no longer exists)',
	'YE': 'Yemen',
	'YT': 'Mayotte',
	'YU': 'Yugoslavia',
	'ZA': 'South Africa',
	'ZM': 'Zambia',
	'ZR': 'Zaire',
	'ZW': 'Zimbabwe',
	'ZZ': 'Unknown or unspecified country',
}

print(countriesDict)

# Read file
filename = "file.txt"

with open(filename) as f:
    content = f.readlines()

numLine = 1
for line in content:
  print(numLine, line)
  numLine += 1


  #if file doesn't exist: -FileNotFoundError prin
# filename = "nonexistent.txt"

# with open(filename) as f:
#     content = f.readlines()

# numLine = 1
# for line in content:
#   print(numLine, line)
#   numLine += 1


# Write File
f = open("test.txt", "a")
f.write("Take it easy")
f.close()




#Nested loops
row1 = ["1L", "1M", "1R"]
row2 = ["2L", "2M", "2R"]
row3 = ["3L", "3M", "3R"]

for position1 in row1:
  for position2 in row2:
    for position3 in row3:
      print(position1, position2, position3)

persons = ["John", "Marissa", "Pete", "Dayton"]

length = len(persons)

for person1 in persons:
  for person2 in persons:
    if(person1 != person2):
      print(person1 + " meets " + person2)

  #If a normal for loop finishes in n steps O(n), how many steps has a nested loop? - O(N * M)







# Slices
pizzas = ['Hawaii', 'Pepperoni', 'Fromaggi', 'Napolitana', 'Diavoli']
mySlice = pizzas[3:4]
print(mySlice)

hello = "Hello World"
print(hello[6:11])




# Multiple Return
def abReturns(a, b):
  abSum = a + b
  print(a, b, abSum)
  return a, b, abSum

abReturns(5, 10)

def fiveReturns(a, b, c, d, e):
  print(a, b, c, d, e)
  return(a, b, c, d, e)

fiveReturns(1, 2, 3, 4, 5)





# Scope
balance = 100
def reduceAmount(withdrawAmount):
  global balance
  print('previous balance:', balance)
  balance -= withdrawAmount

reduceAmount(25)
print('new balance:', balance)

def funcWithLocal(addAmount):
  localVar = 10
  print('previous:', localVar)
  localVar += addAmount
  print('updated:', localVar)

funcWithLocal(15)
# print(localVar)

# Time and date
import time
timenow = time.localtime(time.time())

year,month,day = timenow[0:3]
print(str(year) + '/' + str(month) + '/' + str(day))

  #invalid keyboard input
try: 
  addFive = input("add a number to 5 (must be a number):")
  addFive = int(addFive) + 5
  print(addFive)
except:
  print("Invalid input. Must provide a number")

  #file open error
try:
  open("nonexistent.txt")
except FileNotFoundError:
  print("file does not exist!")
  #when to not use try-except: if there is no error/exception to catch and no need to handle them
  