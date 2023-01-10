import random
from random import randint

def avatar_id_generator():
    characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    length = 5

    _id = "avatar-"

    for _ in range(length):
        _id += random.choice(characters).lower()

    return _id

def otp_generator():
    characters = list("01234566789")

    length = 4

    _id = ""

    for _ in range(length):
        _id += random.choice(characters).lower()

    return _id
