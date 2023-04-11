# // Your last Python3 code is saved below:
def isPalindrome(mystr):
        mystr = ''.join(c for c in mystr.lower() if c.isalnum())
        return mystr == mystr[::-1]
         
# // # # main function
s = "A man a plan a canal Panama"


ans = isPalindrome(s)
# // # # # malayalam
if (ans):
    print("Its a palindrom")
else:
    print("Its not")
