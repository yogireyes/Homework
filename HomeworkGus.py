#Question 1
#Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name + "!")
hello_name("USERNAME")
       
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1, 100):
        if num % 2 != 0:
            print(num)
first_odds() 

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

a_list = [4, 44, 38, 50, 1]

def max_num_in_list():
    maxnumber = max(a_list)
    print(maxnumber)

max_num_in_list()

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if not (a_year % 4):
        if a_year % 100:
            leapyear = True
    else: leapyear = False
    print(leapyear)

is_leap_year(2020)

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
     

a_list = [2,3,4,5,6,7,10]
print(is_consecutive(a_list))