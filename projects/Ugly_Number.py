
"""
Ugly Number : An Ugly Number is a positive number, whose prime factors are only 2, 3, and 5.
Rule:
 Keep dividing the number by 2, 3, and 5 as much as possible:

 - If the final result becomes 1, it is an ugly number.
 - Otherwise, it is not an ugly number.
"""  
 

n = int(input("Enter the number : "))

if n <= 0:
    print("false")

else:
    while n%2 == 0:
        n /= 2
    while n%3 == 0:
        n /= 3
    while n%5 == 0:
        n /= 5

    print(n == 1)   