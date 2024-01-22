import string
from datetime import datetime
from random import random

NULLABLE = {'blank': True, 'null': True}


def generate_password():
    length = 6
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password




