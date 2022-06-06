import random
import string

letters = string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
random.choice(string.ascii_letters)

nums = random.randint(1000,9999)

let = ( ''.join(random.choice(letters) for i in range(4)) )
num = (nums)

print (let,num)
