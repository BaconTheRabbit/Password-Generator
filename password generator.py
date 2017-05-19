import random
import string
def passwordgen(length, count=0, password=''):
	while count < length:
		count += 1
		password = password + random.choice(string.ascii_letters+string.punctuation+string.digits)
	return password
password = passwordgen(int(input('length of password')))
print(password)
input()
