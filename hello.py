name = input("Enter Your name: ")
age = input("Enter your age: ")
school = None

print(f"Name is {name} , Age is {age} , my school is {school}")

print("Name is ", name, " age is " , age)

# srting concaternation

print("Name is " + name + " my age is " + age)

print(type(age))


s= "zamly"

print("z" in s)
print("aml" in s)
print("zmy" in s)

message = "Im Going Out"
print(message.upper())
print(message.lower())
print(message.__len__())
print(message.count('i'))
print(message.find('Out'))

new_message = message.replace("Out", " to the cinema")
print(new_message)

greeting = "Hello"
name = "Michell"

msg = greeting + ', ' + name + ". Welcome!"
msg = "{}, {}. Welcome!".format(greeting, name)

print(help(str.lower))


print(3//2)


arr = ['zam', 'zai', 'zar', 'naj']

arr.insert(2,'naf')

for item in arr:
    print(item)

print()

for ind , item in enumerate(arr, start=1):
    print(ind, item)


# sets

set1 = {'a', 'e', 'i', 'o'}
set2 = {'z', 'a', 'm', 'e'}

print(set1.union(set2))


# Dictionary

student = {'name': 'zamly', 'age': 26, 'subject': ['math', 'IT']}

print(student['name'])


print(student.get('phone', 'Notfound'))

student['phone'] = '555-55555'

print(student.get('phone', 'Notfound'))

# Multiple value Updates

student.update({'name': "jane", "phone": "555-34342"})

print(student)

# del student['age']
age = student.pop('age')

print(student)
print(age)

print(student.items())

for k in student:
    print(k)

for k, val in student.items():
    print(k, val)


# Conditions 

user = "admin"
logged_in = False

if user == "admin" and logged_in:
    print("Welcome")
elif user == "admin" and not logged_in:
    print("pls logging")
else:
    print("Bad cred")

a = [1,2,3]
b =a
b = [1,2,3]

print(id(a))
print(id(b))

print(a == b)
print(a is b)

















