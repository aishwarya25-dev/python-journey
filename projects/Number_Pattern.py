# Number Pattern using if/else and for loop

n = int(input("Enter the no: "))

if not isinstance(n,int):
    print("Argument must be an integer value.")

elif n <= 0 :
    print("Argument must be an integer greater than 0.")

result = []

for i in range(1, n+1):
        result.append(str(i))

print(" ".join(result)) 









    
       


    