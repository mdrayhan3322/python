
# unpack tuple
name = ("rayhan","mamun","reday","reyed")
(a,b,c,d) = name
print(b)
(*a,)= name
print(a)

for i in name:
    print(i)

for j in range(len(name)):
    print(j)

for k in  range(len(name)):
    print(name[k])
