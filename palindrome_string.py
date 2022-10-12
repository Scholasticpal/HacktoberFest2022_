def isPalindrome(string): 
    if len(string) < 1: 
        return True 
    else: 
        if string[0] == string[-1]: 
            return isPalindrome(string[1:-1]) 
        else: 
            return False 
str1 = input("Enter string : ") 
if(isPalindrome(str1)==True): 
   print("The string is a palindrome.") 
else: 
   print("The string is not a palindrome.") 
