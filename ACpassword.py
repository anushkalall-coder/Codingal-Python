import random
import string

def generate_password(length):
    # Combine uppercase, lowercase letters and digits
    characters = string.ascii_letters + string.digits

    # Generates password
    password_list = [random.choice(characters) for _ in range(length)]

    # Shuffles the password
    random.shuffle(password_list)

    # Converts list to string
    password = ''.join(password_list)

    return password

length = 10
print("Generated Password:", generate_password(length))