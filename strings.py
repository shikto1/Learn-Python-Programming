"""
String literals in python are surrounded by either single quotation ('') marks, or double quotation("") marks.
"""
print("Hello")
print('Hello')

# Assigning String to variable
print("")
print("Assigning string to variable>>>")
name = "Shishir"
print(name)

# Assigning Multi line String to variable

"""
# You can assign a multiline string to a variable by using three
 quotes (both single single and double quate are allowed:

"""
address = """
Katigram, Manikganj
Bangladesh
"""
print(address)

# upper()
city = 'dhaka'
print(city.upper()) # Output: DHAKA

# lower()
city = "DHAKA"
print(city.lower()) # Output: dhaka

# len()
city = "dhaka"
print(len(city)) # output: 5

# String are character arrays
cities = "manikganj, dhaka"
print(cities[0]) # Output: m

# strip(): removes any whitespace from the beginning or the end
city = "   dhaka "
print(city.strip()) # Output: dhaka

# replace()
city = "dhaka"
print(city.replace("dh", "t")) # Output: taka

#splits
cities = 'dhaka,manikganj'
print(city.split(", "))

# Check string
address = "dhaka, bangladesh"
print("dhaka" in address)

# String concat
h = "hello"
w = "world"
print(h + " " + w)

# combined string with number with format function
age = 27
txt = "I am {} years old"
print(txt.format(age))

# Also we can pass multiple params with format function
name = "Tannima"
age = 27
txt = "{} is {} years old"
print(txt.format(name, age))

# Use formatted function to concat string with numbers
name = "Tannima"
age = 27
txt = f"{name} is {age} years old"
print(txt)





