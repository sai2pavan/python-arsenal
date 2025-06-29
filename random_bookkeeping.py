"""
random_bookkeeping.py

This script demonstrates Python's random module bookkeeping functions:
- seed()
- getstate()
- setstate()

These functions allow you to control and inspect the internal state of Python’s random number generator.
"""

import random

print("Bookkeeping Functions in random Module")
print("----------------------------------------\n")


# random.seed()

print("=== random.seed() ===")
print("We use seed() to get reproducible results from random functions.\n")

print("Setting the seed to 42...")
random.seed(42)
print("Random number after seed(42):", random.randint(1, 100))

print("Resetting the seed to 42 again...")
random.seed(42)
print("Same random number after seed(42):", random.randint(1, 100))
print("This proves seed() makes randomness predictable.\n")


# random.getstate() & setstate()

print("=== random.getstate() and random.setstate() ===")
print("These functions let us capture and restore the internal RNG state.\n")

print("Seeding RNG with 123 and saving state...")
random.seed(123)
state = random.getstate()

first_number = random.randint(1, 100)
print("First random number:", first_number)

second_number = random.randint(1, 100)
print("Second random number:", second_number)

print("\nRestoring saved state...")
random.setstate(state)

print("Replaying the first number again:", random.randint(1, 100))
print("Replaying the second number again:", random.randint(1, 100))
print("\nThis proves setstate() rewinds the RNG back to a saved point.")
