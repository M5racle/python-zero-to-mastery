# Lecture 30: Stringstype

#print(type('Hi, hello there'))
#user_name = 'Wayne'
#password = 'supersecret'
#long_string = '''
#WOW
#0 0
#---
#'''
#print(long_string)

#first_name = 'Wayne'
#last_name = 'Lumpkin'
#full_name = first_name + ' ' + last_name
#print(full_name)

# Lecture 31: String Concatenation

#'hello' + 'Wayne'
#print( 'Hello'  + ' Wayne' )  
 
#Lecture 32: Type Conversion

#print(type(str(100)))
#print(type(int(str(100))))

#a = str(100)
#b = int(a)
#c = type(b)
#print(c)

# Lecture 33: Escape Sequences

#weather = "It\'s \"kind of\"  sunny" 
#print(weather) 

#weather2 = "\tIt\'s \"kind of\"  sunny"
#print(weather2)

#weather = "\t It's \"kind of\" sunny \n Hope you have a great day"
#print(weather) 

# Lecture 34: Formatted Strings

#name = 'Wayne'
#age = 42
#print('Hi, ' + name + '. You are ' + str(age) + ' years old.')

#name = 'Wayne'
#age = 42
#print(f'Hi, {name}. You are {age} years old.')

#name = 'Wayne'
#age = 42
#print('Hi, {}. You are {} years old.'.format(name, age))

#name = 'Wayne'
#age = 42
#print('Hi, {new_name}. You are {age} years old.'.format (new_name='Jerome', age=21))

# Lecture 35: String Indexes

#selfish = 'me me me'
        #  01234567
# [start:stop]
#print(selfish[7]) 


#selfish = '01234567'
        #  01234567
# [start:stop:stepover]
#print(selfish[0:8:2])

# Lecture 36: Immutability

#selfish = '01234567' 
         #  01234567
#selfish[0] = '8'
#print(selfish)

# String are immutable, meaning they cannot be changed. You can create a new string based on the old one, but you cannot change the original string in place.

#selfish = '01234567'
         #  01234567
#selfish = selfish + '8'
#print(selfish)












