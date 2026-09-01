import requests


# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200


string= "Hello, World!"


first_name= "John"

last_name= "Doe"


full_name= first_name + " " + last_name

long_dash ="-" * 10
print(long_dash)
print(full_name)



len(long_dash)
len(full_name)

age=18
can_vote= age >= 18

print(can_vote)

is_age=age==18
print(is_age)


#logical operators

age=16

has_license=True

can_drive= age >= 16 and has_license
print(can_drive)


age = 25

has_license = False

can_drive = age >= 16 and has_license
print(can_drive)


age = 25
can_drive = age >= 16 or has_license
print(can_drive)


age =26
has_license = True
drunk = True

can_drive = age >= 16 and has_license and not drunk
print(can_drive)


age =26
has_license = True
drunk = False

can_drive = age >= 16 and has_license and not drunk
print(can_drive)

#String manupulation
#fstring

name="Bhavana"

string= f"Hello, {name}!"
print(string)


#changecase

text= "Bhavana Roopa"
print(text.upper())
print(text.lower())

#find and replace

message= "I Love python programming with python"

print("python" in message)
print(message.find("python"))

print(message.startswith("I"))
print(message.endswith("python"))


print(message.find("python"))
print(message.count("python"))

new_message= message.replace("python", "Java")
print(new_message)

#control statement 

temperature= 25

if temperature > 25:
    print("It's a hot day") 
else:
    print("It's a cold day")

temperature =31
if temperature > 30:
    print("It's a  very hot day")
elif temperature > 25:
    print("It's a hot day")
else:
    print("It's a cold day")


#multtiple conditions

age = 25
has_license = True
weekend = False
holiday = True
raining = True

if age >= 18 and has_license:
    print("You can drive")

if weekend or holiday:
    print("no work today !")

if not raining:
    print("lets go outside")



#nested if 
age = 25
has_ticket = True


if has_ticket:
    if age >= 18:
        print("You can enter the concert")
    else:
        print("You cannot enter the concert")
else:
    print("You cannot enter the concert without a ticket")


#Loops


for i in range(5):
    print(i)

#cont from differnt starting points


for i in range(1, 6):
    print(i)

for i in range(0,10,2):
    print(i)


#lists
age = 23
has_license = False

my_list: list[object] = ["Alice", 25, age, True, has_license]

name = my_list[0]
age = my_list[1]




# Changing list
my_list[0]="Bhavana"

my_list.append("Alice")  # Add to end

my_list.remove("Alice")  # Remove by value

my_list.insert(1, "Alice")  # Insert at position

fruits = ["apple", "banana", "orange"]

# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")      # Add to end
fruits.insert(1, "kiwi")    # Insert at position

# Remove items
fruits.remove("banana")     # Remove by value
last = fruits.pop()        # Remove and return last
del fruits[0]              # Remove by index

#list methods
numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy


fruits = ["apple", "banana", "orange"]

# Check if item exists
if "apple" in fruits:
    print("Found apple!")

# Check if list is empty
if fruits:
    print("List has items")  
else:
    print("List is empty")


#dictiionaries

person: dict[str, str | int] = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
}

person["name"] = "Bob"  # Change value

person["license"] = True  # Add new key-value pair


del person["license"]  # Remove key-value pair


person = {"name": "Alice", "age": 30}

# Add or update
person["email"] = "alice@email.com"  # Add new
person["age"] = 31                   # Update existing

# Remove items
del person["email"]              # Remove by key
age = person.pop("age")          # Remove and return
person.clear()                   # Remove all items



# dictionary methods

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"


#  tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

#Accesing items

point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])      # 3
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")


# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!


# set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}


# functions

def greet():
    print("Hello, World!")


greet()


def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's a hot day")
    elif temperature > 20:
        print("It's a nice day")
    else:
        print("It's a cold day")

check_weather()


#local variable 

def calculate_price():
    price = 100  # Local variable
    tax = 0.1
    total = price + (price * tax)
    print(f"Total price: {total}")

calculate_price()

print (price)  # This will raise an error because 'price' is not defined outside the function       


#global variable
discount_rate = 0.15  # Global variable

def apply_discount(price: float) -> float:
    discount = price * discount_rate  # Can read global variable
    return price - discount

result = apply_discount(100)
print(result)  # 85.0

#function with parameters

def calculate_total(price,discount):
    tax_rate=0.08
    tax= price * tax_rate
    final_price= price + tax - discount
    print(f"Final price: {final_price}")

calculate_total(100, 10)  # Final price: 98.0


def add_print(a,b):
    print(a+b)

add_print(5,10)  # 15


#return statement

def add_return(a, b):
    return a + b

result = add_return(5, 10)




def double(number):
    return number * 2


result = double(5)

total = double(10) + double(20)
print(f"Total: {total}")

print (double(5))  # 10

if double(7) > 10:
    print("Greater than 10")

#practice 

def greet_user():
    print("Hello,Alice!")

greet_user()  # Hello, Alice!


def greet(last_name,first_name="John"):
    print(f"Hello, {first_name} {last_name}")

greet(last_name="Roopa",first_name="Bhavana")  # Hello, Bhavana Roopa

#multple parameters

def calculate_total(price,tax_rate,discont):
    tax=price*tax_rate
    final_price=price+tax-discont
    print(f"Final price: {final_price}")

calculate_total(100,0.08,10)  # Final price: 98.0 order matters

#keyword arguments

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)


#return statement

def add(a, b):
    print(a+b)  # This function prints the sum but does not return it ,it does not store the result for later use


def add1(a, b):
    return a + b  # This function returns the sum, allowing it to be stored or used later   

result = add1(5, 10)  # result now holds the value 15

def calculate_area(length, width):
    area = length * width
    return area 

room_area = calculate_area(5, 10)  # room_area now holds the value 50
print(f"Room area: {room_area}")  # Room area: 50

def double(number):
    return number * 2

result = double(5)  # result now holds the value 10

total = double(10) + double(20)  # total now holds the value 60

print(double(15))

  # Prints 30

if double(7) > 10:
    print("Greater than 10")  # This will print because double(7) is 14


#returm multi[ple values

def get_min_max(numbers):
   return min(numbers), max(numbers)  # Returns a tuple of (min, max)

min_value, max_value = get_min_max([1, 2, 3, 4, 5])
print(f"Min: {min_value}, Max: {max_value}")  # Min: 1, Max: 5


result = get_min_max([10, 20, 5, 15])
print(result)  # (5, 20) - a tuple containing the minimum and maximum values


#IMPORT     

import math #import the entire module

print(math.sqrt(16))  # 4.0

from math import sqrt  # Import only the sqrt function

print(sqrt(25))  # 5.0

#random

import random

number =random.randint(1, 10)  # Random integer between 1 and 10
print(number)
choice = random.choice(["apple", "banana", "cherry"])  # Randomly choose from a list
print(choice)   


#datetime operating sustem json data imports


import datetime

today = datetime.date.today()
print(today)  # Prints today's date in YYYY-MM-DD format

import os

current_directory = os.getcwd()  # Get current working directory
print(current_directory)

import json

data = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(data)  # Convert dictionary to JSON string


print(json_string)  # Prints the JSON string

import requests

latitudde = 40.7128
longitude = -74.0060

url=f"https://api.open-meteo.com/v1/forecast?latitude={latitudde}&longitude={longitude}&current_weather=true"


response = requests.get(url)
data=response.json()

print(data)


type(data)
data.keys()


data["current_weather"]["temperature"]



#functions and api 


import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
    data = response.json()
    return data["current_weather"]["temperature"]

paris_temp=get_weather(48.8566, 2.3522)  # Paris coordinates
new_york_temp=get_weather(40.7128, -74.0060)
london_temp=get_weather(51.5074, -0.1278)

print(f"Current temperature in Paris: {paris_temp}°C")
print(f"Current temperature in New York: {new_york_temp}°C")
print(f"Current temperature in London: {london_temp}°C")
