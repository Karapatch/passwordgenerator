import random
from string import ascii_lowercase, ascii_uppercase, ascii_letters

lenght = int ( input () )
password = ''

for i in range ( 0 , lenght ) :
    password = password + random.choice(ascii_uppercase)

print ( 'Your password : ' , password )
