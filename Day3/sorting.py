li = [1,3,-5,6,-7,2,4,9,8]

# s_li = sorted(li, reverse=True)

s_li = sorted(li, key=abs)

print('Sorted variable: \t', s_li)

li.sort()
# li.sort(reverse=True)

print('Original variable: \t', li)

print("\n\n\n")

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f'({self.name}, {self.age}, {self.salary})'


e1 = Employee('Carl', 34, 70000)
e2 = Employee('Sarah', 84, 80000)
e3 = Employee('AJohn', 44, 90000)

employees = [e1, e2, e3]

# def e_sort(emp):
#     return emp.name

# s_employees = sorted(employees, key=lambda e: e.name)


from operator import attrgetter

s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)




