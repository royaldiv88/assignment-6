#check whether the program is panagram or not
str=input("Enter the string to be checked=")
alphabet="abcdefghijklmnopqrstuvwxyz"

flag=True
for char in alphabet:
    if char not in str.lower():
        flag=False
if flag==True:
    print("It is a pangram")
else:
    print("It is not a pangram")
