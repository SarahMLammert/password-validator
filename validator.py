import re

# Contains at least one number, one special symbol, and one uppercase and one lowercase letter
# Is 6-20 characters long
regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
pattern = re.compile(regex)

while True:
    password = input('Your password: ')
    match = pattern.search(password)
    if match == None:
        print('Your password wasn\'t valid.\n Please type a different password.')
    else:
        print('Your password is valid.')
        break
