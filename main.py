# units = 24
# name_of_unit = "hours"
#
# # Function with parameters
#
#
# def days_to_units(num_of_days, message):
#     print(f"{num_of_days} days are {num_of_days * units} {name_of_unit}")
#     print(message)
#
# days_to_units(20, "Perfect")
# days_to_units(30, "Perfect")

# b, c, d = 5, 6.4, "Great"
# print(f"{b} is integer and {c} is float and {d} is string")

#
# w = int(5)
# x = str(5)
# y = "five "
# z = float(5)
#
# print(w)
# print(x)
# print(y)
# print(z)
# print(w, x, y, z)
#
# a = "Apple "
# b = "is "
# c = "red "
# d = 5
# e = "is a number"
# print(a + b + c)
# print(d, e)

# How to code for when need 'Input' from the users using input() function for data types: string, number and float

# name = input("Enter name: ")
# print(type(name))

# number = int(input("Enter number: "))
# print(type(number))

# name = input("Enter name: ")
# print("My name is", name)

# language = "Python"
# print("1.", language == "python")
# age = 18
# print("2.", age >= 18)
# print("3.", age > 18)
# print("4.", age >= 18 or language == "Java")

# If Else statements

# score = int(input("Enter your score: "))
#
# if score >= 50:
#     print("You have passed your exams")
#     print("Congratulations")
#
# else:
#     print("You have failed your exams")
#     print("Hard work next time")

# score = 50
#
# if score >= 50:
#         print("You score is:", score)
#         print("Congratulations")
#
# else:
#         print("You have failed your exams")
#         print("Hard work next time")


# If Else Elife statements

# score1 = 48
# score2 = 54
#
# if score1 >= 49:
#         print("You score is:", score1)
#         print("Congratulations")
#
# elif score2 >= 55:
#         print("You score is:", score2)
#         print("Congratulations")
# else:
#         print("You have failed your exams")
#         print("Hard work next time")


# subject1 = "maths"
# score1 = 50
# subject2 = "science"
# score2 = 50
#
# if subject1 == "maths" and score1 == 49:
#         print("maths is pass")
#
# elif subject2 == "science" and score2 == 50:
#         print("science is pass")
#
# else:
#         print("Invalid Subjects")

# number = float(input("Enter number:"))
#
# if number >= 0:
#         print("The number is positive", number)
# if number <= 0:
#         print("The number is negative", number)
# if number ==0:
#         print("The number is zero", number)


# While Loop Statement

# count = 0
#
# while count < 5:
#         print(count)
#         count = count + 1

# count = 5
#
# while count <= 15:
#         print(count)
#         count = count + 1

# number = int(input("Enter a number: "))
#
# count = 1
# while count <= 10:
#         product = number * count
#         print(number, "x", count, "=", product)
#         count = count + 1


# number = int(input("Enter a number: "))
#
# count = 10
# while count >= 1:
#         product = number * count
#         print(number, "x", count, "=", product)
#         count = count - 1


# For Loop Statement

# text = "Python"
#
# for text in text:
#     print(text)
#
# text = "Python"
#
# for character in text:
#     print(character)

# Loop through sequence (list) and range

# number = int(input("Enter an integer: "))

# for count in range(1, 11):
#     product = number + count
#     print(number, "+", count, "=", product)

# x = int(input("Enter an integer: "))
#
# for y in range(1, 11):
#     z = x + y
#     print(x, "+", y, "=", z)

# Break and Continue

# for x in range(1, 10):
#     if x == 5:
#         break
#     print(x)
# print("The end")

# while True:
#         number = float(input("Enter a number: "))
#         if number < 0:
#                 break
#         print("You entered: ", number)

# Continue loop

# for i in range(5):
#         number = float(input("Enter a number: "))
#
#         if number > 0:
#             continue
#         print(number)



# languages = "Python", "Java", "Swift", "C", "C++"

# for language in languages:
#         if language == "Python":
#                 print(language)
#                 continue
#         if language == "Java":
#                 print(language)
#                 continue
#         if language == "C":
#                 print(language)

# Pass Statement

# number = 5
#
# if number > 0.0:
#      pass

# Functions and arguments

# def greet():
#
#     print("hello")
#     print("hi")
#
#     greet()

# def greet(name):
#
#     print("hello", name)
#     print("hi", name)
#
# greet("sam")

# def add_numbers(x1, x2):
#
#         result = x1 + x2
#         print("Sum is:", result)
#
# number1 = 2.5
# number2 = 2.5
# add_numbers(number1, number2)


# def add_numbers(x1, x2):
#          result = x1 + x2
#          return result
# number1 = 2.5
# number2 = 2.5
# result = add_numbers(number1, number2)
# print("Sum is:", result)

# marks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# length = len(marks)
# print(length)
#
# sum_marks = sum(marks)
# print(sum_marks)

# function to find average marks and call it outside the function

# def find_avg_marks(marks):
#         sum_of_marks = sum(marks)
#         total_subjects = len(marks)
#         avg_marks = sum_of_marks / total_subjects
#         return avg_marks
#
# # function to compute grade and call it outside the function
#
# def compute_grade(avg_marks):
#         if avg_marks >= 80:
#                 grade = 'A'
#         elif avg_marks >= 60:
#                 grade = 'B'
#         elif avg_marks >= 50:
#                 grade = 'C'
#         else:
#                 grade = 'F'
#         return grade
#
# marks = [55, 64, 75, 80, 65]
# avg_marks = find_avg_marks(marks)
# print("Your average marks is:", avg_marks)
#
# grade = compute_grade(avg_marks)
# print("Your grade is:", grade)


# function to add two numbers and call it outside the function

# def add_numbers(numbers):
#         sum_of_numbers = sum(numbers)
#         return sum_of_numbers
#
# def multiply_numbers(x, y):
#         multiply = x * y
#         return multiply
#
# def subtract_numbers(x, y):
#         subtract = x - y
#         return subtract
#
# numbers = [5, 5]
# x = 10
# y = 5
#
# sum_of_numbers = add_numbers(numbers)
# print("Addition results is:", sum_of_numbers)
# multiply = multiply_numbers(x, y)
# print("Multiplication results is:", multiply)
# subtract = subtract_numbers(x, y)
# print("Subtraction result is", subtract)


# # calculate average score and based on marks distribute prizes, prize A if avg score >= 90, prize B if avg score >=70, prize c is avg score >=50
#
# def avg_score(score):
#         sum_of_score = sum(score)
#         total_score = len(score)
#         avg_score = sum_of_score / total_score
#         return avg_score
#
# def prize(avg_score):
#         if avg_score >= 90:
#                 prize = 'A'
#         elif avg_score >= 70:
#                 prize = 'B'
#         elif avg_score >= 50:
#                 prize = 'C'
#         else:
#                 prize = 'None'
#         return prize
#
#
# score = [10, 50, 45, 135, 175]
# avg_score = avg_score(score)
# print("Your average score is", avg_score)
# prize = prize(avg_score)
# print("Your prize is", prize)


# # Positional, Keywords and Default Arguments
#
# def add_numbers(x=10, y=20):
#         sum = x + y
#         return sum
#
# sum = add_numbers(20)
# print(sum)


# Python Local and Global Variables
# def add_numbers(x, y):
#         sum = x + y
#         return sum
#
# output = add_numbers(2, 5)
# print(output)


# Global Variable is a variable which is defined outside the function

# example of local variable

# def add_numbers(x, y):
#         result = x + y
#         return result
#
# output = add_numbers(2, 5)
# print(output)

# example of global variable

# message = "hello from outside?"
#
# def greet():
#         message = 'hello from inside'
#         print("This is", message)
# greet()
# print("This is", message)


# Lists are mutable which means can be changed or modify and Tuples which means can't be changed or modify

# list of integers
# list_numbers = [1, 2, 3, 4, 5]
# print(list_numbers)
#
# # mixed list
# random_list = [2.5, "hello", -5, 1.10]
# print(random_list)
#
#
# languages = ["Python", "Java", "Swift", "C", "C++"]
# print(languages[3])
# print(languages[-2])
# print(languages[0:3])
# print(languages[0:6])
# print(languages[:3])
# print(languages[1:])
#
# languages = ["Python", "Java", "Swift", "C", "C++"]
# languages[1] = "Ruby"
# languages[0:5] = ["jython", "kava", "dwift", "D", "D++"]
# print(languages)

# Iterating through list
# languages = ["Python", "Java", "Swift", "C", "C++"]
# show = "Java" in languages
# print(show)

# for language in languages:
#         print(language)

# # append list
# languages = ["Python", "Java", "Swift", "C", "C++"]
# print(languages)
# languages.append("rust")
# print(languages)
# languages.insert(6, "ruby")
# print(languages)
# languages.remove("ruby")
# print(languages)
# languages.remove("rust")
# print(languages)

# Tuples are immutable which means which can't change or modify it
# numbers = (21, 20, -4, 10)
# print (numbers)
# print (numbers[1:])
# for number in numbers:
#         print(number)

# # Strings (text type)
# quote = "Talk is cheap. Show me the code."
# print("1.", quote[3])
# print("2.", quote[-3])
# print("3.", quote.replace("code", "program"))

# # Dictionaries
#
# cars = {"honda": "CRV", "mazda": "cx9" }
# print(cars)
#
# print(cars["honda"])
# cars["bmw"] = "x5"
# print(cars)
# cars.pop("mazda")
# print(cars)

# # Python Sets
#
# animals = {"dog", "cat", "tiger", "dog"}
# animals.discard("cat")
# animals.add("caty")
# print(animals)



# result = list(range(3, 31, 3))
# print(result)
#
# ranges = (3, 11)
# for range in ranges:
#     print(range)

# Object Oriented Programming

# When working with objects, variables are called attributes and functions are called methods.
# student1 and student2 are objects with class as student

# class Student:
#     def validate_marks(self):
#         if self.marks >= 60:
#             return True
#         else:
#             return False
#
#     def __init__(self, name, marks, subject):
#         self.name = name
#         self.marks = marks
#         self.subject = subject
#
#
# student1 = Student("Harry", 80, "Maths")
# student2 = Student("Tom", 55, "Maths")
# print("Student name is", student1.name)
# print("Harry scored", student1.marks, "Marks")
# print("and the subject is", student1.subject)
# did_pass = student1.validate_marks()
# print(did_pass)
# print("Student name is", student2.name)
# print("Tom scored", student2.marks, "Marks")
# print("and the subject is", student2.subject)
# did_pass = student2.validate_marks()
# print(did_pass)



# did_pass = student1.validate_marks()
# print(did_pass)


# student1 = Student()
# student1.name = "Harry"
# student1.marks = 80
# student2 = Student()
# student2.name = "Harry"
# student2.marks = 40
#
# # print(student1.name)
# # print(student1.marks)
#
# did_pass = student1.validate_marks()
# print(did_pass)
# did_pass = student2.validate_marks()
# print(did_pass)

# class home:
#
#     def __init__(self, brickcolor, rooftype, age):
#         self.brickcolor = brickcolor
#         self.rooftype = rooftype
#         self.age = age
#
#     def house_age(self):
#         if self.age >= 10:
#             return True
#         else:
#             return False
#
#
# home1 = home("black", "wood", 9)
# print("Brick color is", home1.brickcolor)
# print("Roof type is", home1.rooftype)
# print("Home is", home1.age, "years old")
# home_age = home1.house_age()
# print("because house is less than 10 years old:", home_age)
# home2 = home("red", "steel", 50)
# print("Brick color is", home2.brickcolor)
# print("Roof type is", home2.rooftype)
# print("Home is", home2.age, "years old")
# verify_home_age = home2.house_age()
# print("because house is more than 10 years old:", verify_home_age)



# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         p = [self.a, self.b, self.c]
#         t = sum(p)
#         return t
#
#
# t1 = Triangle(5, 6, 7)
# print(t1.a)
# print(t1.b)
# print(t1.c)
# total_perimeter = t1.perimeter()
# print(total_perimeter)


# # Inheritance (Base/Parent class > child classes)
#
# class Vehicle:
#         def color(self):
#             print("color is grey")
#
# class honda(Vehicle):
#         def body_type(self):
#             print("This is SUV")
#
#
# class mazda(Vehicle):
#         def body_type(self):
#             print("This is sedan")
#
# v = Vehicle()
# v.color()
#
#
#
# h = honda()
# h.body_type()
# h.color()
#
# m = mazda()
# m.body_type()
# m.color()
#
#
# import math
# # print(dir(math))
#
# a = 25
# result = math.sqrt(a)
# print(result)

# def solveMeFirst(a,b):
# 	# Hint: Type return a+b below
#     a = int(input())
#     b = int(input())
#     return a + b
#
# res = solveMeFirst(2, 3)
# print(res)

# how to work with files in Python

# f = open("qa1.csv", "r")
#
# content = f.read()
# print(content)
#
# f.close

# with open("qa1.csv", "r") as f:
#     content = f.read(1000)
#     print(content)

# how to write to file in Python

# with open("qa1.csv", "w") as f:
#     f.write("2022-11-16 00:00:00.000,2NS12,GRN,DNW,Trucking,060_GRN_571_499_STP,FN3 PASS,LHOLEOPEN,O,Production Blasted Stocks,O,Ore Passes,49.6428,44.860411,2.193206,0.341589,0.163885,5.671438,13.707995,0,0.202641,0.233562,24.383837,0.533456,58.690882,3.010713,2.978276,0.736401,Location,a2")
# with open("qa1.csv", "r") as f:
#     content = f.read()
#     print(content)

# how to append file in Python

# with open("qa1.csv", "a") as f:
#     f.write("\n2022-11-17 00:00:00.000,2NS12,GRN,DNW,Trucking,060_GRN_571_499_STP,FN3 PASS,LHOLEOPEN,O,Production Blasted Stocks,O,Ore Passes,49.6428,44.860411,2.193206,0.341589,0.163885,5.671438,13.707995,0,0.202641,0.233562,24.383837,0.533456,58.690882,3.010713,2.978276,0.736401,Location,a2")
# with open("qa1.csv", "r") as f:
#     content = f.read()
#     print(content)


# # how to write lines in file in Python
#
# with open("qa1.csv", "a") as f:
#     lines = ["\n2022-11-18", "\n2022-11-19", "\n2022-11-20"]
#     f.writelines(lines)
# with open("qa1.csv", "r") as f:
#     content = f.read()
#     print(content)

# # Open / change /rename /remove directories
#
# import os
#
# current_dir = os.getcwd()
# print(current_dir)
#
# current_dir = os.getpid()
# print(current_dir)
#
# # os.mkdir("test")
# os.rename("testnew1", "testnew2")

# Iterators and Iterables

# n = [1, 2, 3]
# # print(dir(n))
#
# value = n.__iter__()
# item1 = value.__next__()
# print(item1)

# OR

# n = [1, 2, 3]
# value = iter(n)
#
# item1 = next(value)
# print(item1)
# item2 = next(value)
# print(item2)
# item3 = next(value)
# print(item3)

# list = [1, 5, 7, 9]
# iter_obj = iter(list)
# while True:
#     try:
#         element = next(iter_obj)
#         print(element)
#     except:
#         break


# with open("raw1.csv", "r") as f:
#     mylist = []
#     content = f.read()
#     # i = iter(content)
#     for row in content:
#         mylist.append(row)
#         # if row == 'T':
#         print(row)

# How to open read CSV files

# import csv
#
# def load_data(filename):
#     mylist = []
#     with open(filename) as f:
#         data = csv.reader(f, delimiter=',')
#         next(data)
#         for row in data:
#             mylist.append(row)
#         return mylist
#
# new_list = load_data("raw1.csv")
# i = iter(new_list)
# for row in i:
#     # if row == 'DSE':
#     print(row)




    # for i in content:
    #     if i == "BLU":
    #         print(i)
    #     else:
    #         print("not found")
    # iter = iter(content)
    # print(content)
    # print(iter)
    # value = iter(content)
    # element = next(value)
    # for i in value:
    #     if i >= "1":
    #         print(i)
    # while(True):
    #     try:
    #         element = next(value)
    #         # print(element)
    #         for i in element:
    #             if i == "Trucking":
    #                 print(i)
    #     except:
    #         break

# value = [1, 1.23562, 1, 1, 1]
# for i in value:
#     if i == 1.23562:
#         print(i)
#     else:
#         print("N")


# def add(x, y):
#     print(x*y)
# add(2,4)



# class Test:
#     def __init__(self, name, price, location, state):
#         self.name = name
#         self.price = price
#         self.location = location
#         self.state = state
#
#     def test_cost(self):
#         if self.price <= 100:
#             print("Affordable")
#             return True
#         else:
#             print("Expensive")
#             return False
#
#     def test_loc(self):
#         if self.state == "wa":
#             print("State is wa")
#             return True
#         else:
#             print("State is not wa")
#             return False
#
#
# suburb1 = Test("perth", 100, "west", "wa")
# suburb2 = Test("sydney", 120, "south", "vic")
#
# print("Suburb1 is:", suburb1.name)
# print("Suburb1 is:", suburb1.location)
# print("Suburb1 is:", suburb1.state)
# print("Suburb2 is:", suburb2.name)
# print("Suburb2 is:", suburb2.location)
# print("Suburb2 is:", suburb2.state)
# cost_suburb = suburb1.test_cost()
# print(cost_suburb)
# cost_suburb = suburb2.test_cost()
# print(cost_suburb)
# loc = suburb1.test_loc()
# print(loc)
# loc = suburb2.test_loc()
# print(loc)
#
#
# def test_add():
#     x = 5
#     y = 10
#     z = x + y
#     print(z)
#
#
# test_add()



class Test:
    def __init__(self, n1, n2, age):
        self.n1 = n1
        self.n2 = n2
        self.age = age

    # def test_age(self):
    #     if self.age >= 40:
    #         print("Correct")
    #         return True
    #     else:
    #         print("Incorrect")
    #         return False

info = Test("Vivek", "Sharma", 40)
print(info.n1)
print(info.n2)
# age_test = info.test_age()
# print(age_test)