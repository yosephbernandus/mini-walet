import re
import string
import random

letters = re.sub("[BDOIMN]", "", string.ascii_letters)
digits = re.sub("[01]", "", string.digits)


def generate_random_number(length: int = 64) -> str:
    return "".join(random.choices(letters + digits, k=length))
