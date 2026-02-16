
my_str_1 = 'Hello'
my_str_2 = "World"

my_str_3 = """Multiline
String"""
my_str_4 ='''Another
multiline
String'''

print(my_str_3)
print(my_str_4)

msg = "It's a sunny day!"
msg_2 = 'She said, "Hello World!"'

print(msg, msg_2)

msg_3 = "It\'s a sunny day!"
msg_4 = "She said, \"Hello World!\""

print(msg_3, msg_4)

#---------------------------------------------------------------

my_str = 'Hello World'
print('Hello' in my_str)
print('hey' in my_str)
print('hi' in my_str)
print('e' in my_str)
print('f' in my_str)

#---------------------------------------------------------------

my_str = 'Hello World'
print(len(my_str))

print(my_str[0], my_str[1])
print(my_str[-1], my_str[-2])

#---------------------------------------------------------------

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

greeting = 'hey'
#greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

#---------------------------------------------------------------

my_str_1 = 'Hello'
my_str_2 = "World!"
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)

name = 'John Doe'
age = 26

#name_and_age = name + age # TypeError: can only concatenate str (not "int") to str
name_and_age = name + str(age)
print(name_and_age)

name = "Doe John"
age = 25
name_and_age = name
name_and_age += str(age)
print(name_and_age)

name = 'John Doe'
age = 25
#f : formatted string
name_and_age = f'Name is {name} and age is {age}'

num1 = 5
num2 = 10
print(f'Sum of {num1} and {num2} is {num1 + num2}') #Note how you don't need to convert non-string types with the str() function. In the example

#---------------------------------------------------------------

my_str = 'Hello World'
print(my_str[1:4])
print(my_str[:7])
print(my_str[8:])
print(my_str[:])
print(my_str[0:8:2])
print(my_str[::-1])

#---------------------------------------------------------------

my_str = 'hello world!'
print(my_str.upper())

my_str = 'HELLO WORLD!'
print(my_str.lower())

my_str = '    hello world         '
print(my_str.strip())

my_str = 'hello world'
print(my_str.replace('hello', 'hi'))

split_words = my_str.split()
print(split_words)

my_list = ['hello', 'world']
print(' '.join(my_list))

print(my_str.startswith('hello'))
print(my_str.endswith('world'))

print(my_str.index('world'))

o_count = my_str.count('o')
print(o_count)

print(my_str.capitalize())

print(my_str.title())

#---------------------------------------------------------------

is_upper = my_str.isupper()
print(is_upper)

is_lower = my_str.islower()
print(is_lower)

#---------------------------------------------------------------