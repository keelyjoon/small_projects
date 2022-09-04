import pytest

def primes_up_to_n(n):
   '''parameter :
          n - integer
          
   returns a list of all primes <= n
   returns None if n is not an integer
   '''
   if type(n) is not int:
      return None
   else:
      list_of_primes = []
      for potential_prime in range(2,n+1):
         #print("potential prime",potential_prime)
         could_be_prime = True
         done = False
         possible_divisor = 2
         while could_be_prime and possible_divisor < potential_prime:
            #print("\tpossible divisor",possible_divisor)
            if potential_prime % possible_divisor == 0:
               could_be_prime = False
               is_prime = False
            else:
               possible_divisor += 1
               
         if possible_divisor == potential_prime:
            list_of_primes.append(potential_prime)
            
      return list_of_primes

"""
$test_primes1() tests the primes_up_to_n()
with a list of two ints. Because the function 
was expecting an int,
This test is expected to pass returning None
"""
def test_primes1():
    assert primes_up_to_n([11,29]) == None

"""
$test_primes2() tests the primes_up_to_n()
with an int. This test is expected to pass,
returning a list of all the prime numbers up
to 36.
"""
def test_primes2():
   assert primes_up_to_n(36) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

"""
$test_primes3() tests the primes_up_to_n()
with a float. Because this is not an int,
the test is expected to pass returning None
"""
def test_primes3():
   assert primes_up_to_n(36.0) == None

"""
$test_primes4() tests the primes_up_to_n()
with an int of 1. Because there are no prime
numbers before or including 1, this test is 
expected to pass returning an empty list
"""
def test_primes4():
   assert primes_up_to_n(1) == []

"""
$test_primes5() tests the primes_up_to_n()
with an int of 13. Because 13 is a prime number, 
this test is expected to pass returning a list of 
all the prime numbers up to and including 13.
"""
def test_primes5():
   assert primes_up_to_n(13) == [2,3,5,7,11,13]