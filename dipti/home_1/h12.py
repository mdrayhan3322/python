
# problem:  Python Program to Check Leap Year

year = int(input("Enter a year "))
if year % 400 == 0 :
     print("Leap year ")
elif  year % 100 == 0:
     print("not leap year ")
elif year % 4 == 0:
     print("Leap year ")
else : print(" Not leap year ")
