# palindrome
string = 'afif waliyudin'
def is_palindrome(string):
    string = string.replace(" ","").lower()
    return string == string[::-1]
if is_palindrome(string):
    print(string + " adalah palindrome")
else:
    print(string + " bukanlah palindrome")