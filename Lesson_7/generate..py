from random import choices, randint
import os

LETTERS = "asdfgjklqwertyuiopzxcvbnm"


def files_create(ext, min_length=6, max_length=30, min_bytes=256, max_bytes=4096, files_amount=42):
    for _ in range(files_amount):
        filename = str(choices(LETTERS, k=(randint(min_length, max_length)))) + ext
        with open(filename, 'wb') as f:
            f.write(os.urandom(randint(min_bytes, max_bytes)))

files_create(".bin")
