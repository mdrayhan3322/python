
class Calculator:
    brand = "Casio MS990"
    def sum(self,n1,n2):
        return n1+n2
    def sub(self,n1,n2):
        return n1-n2
    def mul(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):
        return n1/n2

# difind object declaier 
calculator = Calculator()
print(calculator)
print(calculator.brand)
print(calculator.sum(20,10))
print(calculator.sub(10,20))
print(calculator.mul(20,10))
print(calculator.div(20,10))