
# problem: Python Program to Check Prime Number
number = int(input("Enter a number "))
if number <0 or number ==0  or number == 1:
    print("Number is  not a  prime Number ")
elif number % number  == 0 and number%2  != 0 :
    print("prime number ")
else:print("Not pime number")