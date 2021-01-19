import random
import string
def generate_code():
    a=''
    for i in range(4):
        a+=random.choice(string.ascii_letters)
    return a

  