from math import *


upper_bound = int(input("Range of unique primes to calculate? "))
primes = [2]

def is_prime(number):            
    denominator = 2
    while denominator <= sqrt(number):
        if number % denominator == 0:
            return False
        denominator += 1
    return True

for index in range(3, upper_bound):
    if index % 2 != 0:
        if is_prime(index): 
            #print('{0} : prime'.format(n)) 
            primes.append(index)  
    if len(primes) == 100000000:
        break
            
print('There are {0} primes from 1 to {1}. The last prime is {2}'.format(len(primes),upper_bound,primes[-1]))