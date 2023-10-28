"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number):
    state = False
    for i in range (2,number):
        if number % i == 0:
            state = False
            break
        else:
            state = True
    return state
            
def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"number_of_primes= {number_of_primes} should have been a positive number.")
    list = [2]
    count = 2
    while len(list) < number_of_primes:
        if is_prime(count):
            list.append(count)
        count += 1
    return list
