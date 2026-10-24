from faker import Faker
from faker_food import FoodProvider
import random

fake = Faker()
fake.add_provider(FoodProvider)

def generate_ingredient():
    ingredient = fake.ingredient()
    return ingredient

def random_type_ingredient():
    type_ingredient = random.choice(['SAUCE', 'FILLING'])
    return type_ingredient

def generate_price():
    price = random.randint(1, 100) * 10
    return price