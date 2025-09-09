
""" 
def full_name(first_name,last_name):
    name = f"{first_name} {last_name}"
    return name
name = full_name("md","rayhan")
print(name)

 """
# ---------------------------
""" 
def ching_name(first_name,last_name):
    name = f"{first_name} {last_name}"
    return name
name = ching_name(last_name="rayhan",first_name='Md')
print(name)

 """

# --------------

def a(last,title,*first):
    name = f"{title} {last} {first}"
    return name
name = a(last="rayhan",title="eng")
print(name)