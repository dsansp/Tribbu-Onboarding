import random

def generate_valid_dni():
    # 1. Genera 8 dígitos aleatorios
    numbers = "".join([str(random.randint(0, 9)) for _ in range(8)])
    
    # 2. Calcula la letra (Algoritmo Módulo 23)
    mapping = "TRWAGMYFPDXBNJZSQVHLCKE"
    letter = mapping[int(numbers) % 23]
    
    return f"{numbers}{letter}"