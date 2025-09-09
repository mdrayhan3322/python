


""" 
def sum (num1,num2,num3=0 , num4=0,num5=0):
    result = num1+num2+num3+num4+num5
    return result
ans = sum(29,29,2)
print(ans)

 """
# agrs
def a(*number):
    print(number)
    sum = 0
    for a_valu in number:
       sum = sum+a_valu
    return sum
total = a(3,3,5,3,32) 
print(total) 