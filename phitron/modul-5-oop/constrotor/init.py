

class Phone:
    manufactured = "china"

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price


my_phone = Phone("kala chand","Oppo",20000)
print(my_phone)
print(my_phone.__init__)

print(my_phone.brand,my_phone.owner,my_phone.price)

