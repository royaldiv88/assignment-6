#check whether a passed string is palindrome
a=str(input("enter any string - "))
if (a[-1::-1]==a):
    print ("the word is palindrome")
else:
    print("not a palindrome")
