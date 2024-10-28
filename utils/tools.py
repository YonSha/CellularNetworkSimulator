import random
import string


def generate_sim_code(length=10) -> str:
    characters = string.ascii_letters + string.digits  # Letters and digits
    sim_code = ''.join(random.choice(characters) for _ in range(length))
    return sim_code


def generate_ip_addresses(init_number):
    init_number += 1
    return init_number
