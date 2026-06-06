# Take an input of string
string = str(input("Enter the word to reverse: "))

# 1. reverse it by using "SLICE"
print(string[::-1])

# # 2. reverse it by using "reversed()" an "".join()
rev = "".join(reversed(string))
print(rev)

# 3. looping
reversed_text = ""
for char in string:
    reversed_text = char + reversed_text

print(reversed_text)
    

