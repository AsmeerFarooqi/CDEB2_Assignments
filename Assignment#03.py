'''Q#01
vowels = input("Enter the  vowels:").lower()
list =[]
for list in vowels:
    print (list)'''

'''Q#02'''

'''name = input("Enter any name :")
if len(name) >1:
    name1 = name[0] 
    name2 = name[-1]
    name3= name[1:-1]
    all_characters = name2 + name3 + name1
    print("modified string", all_characters)
else:
    print("false string")
'''
'''Q#03'''
'''user_string = input("Enter a string:")

if len(user_string)>1:
    string = user_string[::-1]
    print("modified string:" , string)'''

'''Q#04'''
'''user_string = input("Enter a string:")
if len (user_string)>1:
    shifted_string = user_string[1:] + user_string[0]
    
    print("modified string:" , shifted_string)
'''
'''Q#05'''
'''user_string = input("Enter a string:")
uppercase_count =0
lowercase_count =0
digit_count = 0
whitespace_count =0

for char in user_string:
    if char.isupper():
        uppercase_count += 1
        
    elif char .islower():
        lowercase_count +=1
       
    elif char .isdigit():
        digit_count +=1
        
    elif char .isspace():
        whitespace_count +=1
        
    
print("Uppercase_count:",uppercase_count)
print("Lowercase_count:", lowercase_count)
print("digit_count:", digit_count)
print("whitespace_count:", whitespace_count)'''

'''Q#06'''

'''name = input("Enter your name:")

initials = name[0]
for i in range (len(name)):
    if name[i] == ' ':
        initials += name[i+1]
initials = initials.upper()
print("Initials: ", initials)
'''

'''Q#07'''
'''pallindrome = input("Enter a string:")

reversed_version = pallindrome[::-1].lower() 
if reversed_version == pallindrome: 
    print("It is a pallindrome.")
else:
    print("Not a pallindrome.")'''

'''Q#08'''

'''ords = "shift"
for i in range(len(words)):
    words= words[1:] + words[0] 
    print("modified string:" ,words)'''

'''SHIFT  HIFTS iftsh
    01234  01234 01234'''

'''Q#09'''
'''password = input("Enter your password:")

is_small = False
is_big = False
is_num = False
password_length = len(password)>=8

for words in password:
    if words.isupper():
        is_big = True
    if words.islower():
        is_small = True
    if words.isdigit():
        is_num= True
    if password_length >=8:
        password_length =True
    
if (is_small and is_big and is_num and password_length):
    print("Password is valid.")
else:
    print("Password is invalid.")'''