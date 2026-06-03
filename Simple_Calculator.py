# SIMPLE CALCULATOR
# USING CLASS

# Created the class as calculator
class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def power(self,a,b):
        return a**b
    def div(self,a,b):
        i = (a/b if b!=0 else "You can't divide by zero!!") 
        
# Created the object
cal = calculator()

# Taking user input 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Listing operation to perform
print("----SIMPLE CALCULATOR----")
print("Choose operation no.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Power")
print("5.Division")

# Taking user choice as an integer
choice = int(input("Enter the number of operation to perform: "))

if choice == 1:
    print("Result = ",cal.add(a,b))
elif choice == 2:
    print("Result = ",cal.sub(a,b))
elif choice == 3:
    print("Result = ",cal.mul(a,b))
elif choice == 4:
    print("Result = ",cal.power(a,b))
elif choice == 5:
    print("Result = ",cal.div(a,b))
else:
    print("Invalid choice!!")
     



