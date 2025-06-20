import random
import string


def generate_random_email(domain="example.com", length=8):
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    return f"{username}@{domain}"
