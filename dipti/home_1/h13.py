
# Python Program to Find the Largest Among Three Numbers
a = int(input("Enter number one "))
b = int(input("Enter number tow "))
c = int(input("Enter number three "))

if a == b :
    print((f"a {2} and b {b} is equeal "))
    if a>c:
        print("a and b large nuber c ")
    elif c>a:
        print(" c is larges number a and b")
   
elif b == c :
    print(f"b {b} and c {c} is equal ")
    if b>a:
        print(f"b {b} is grater then a {a}")
    elif a>b:
        print(f"a {a} is grater then b {b}")

elif c == a :
    print(f"c {c} and a is equal ")
    if c>b:
        print(f"c {c} is grater then b {b} ")
    elif b<c:
        print(f"b {b} is grater then c {c} ")
else:
    if a>b and a>c:
        print(f"a {a} is grater then b {b} and c {c}")
    elif b>a and b>c:
        print(f"b {b} is grater then a {a} and c {c}")
    else : print(" c is large number a and b ")

