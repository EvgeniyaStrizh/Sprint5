import random
import string

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

def generate_random_email(domain="example.com", length=8):
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    return f"{username}@{domain}"


 
