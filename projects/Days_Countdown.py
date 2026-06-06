# Days countdown using class

class date:
    def __init__(self, first):
        self.first = first
    
    def __sub__(self, second):
        return self.first - second.first

date_1 = int(input("Enter first date : "))
date_2 = int(input("\nEnter second date : "))

print(f"\nThe days between {date_1} and {date_2} = {abs(date_1 - date_2)}")
