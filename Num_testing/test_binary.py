import pytest

def binary_string(n):
   '''parameter:
         n - integer
         
      returns a string of "0"s and "1"s giving the binary representation of n
      returns None if n is not an integer
   '''
   
   if type(n) is not int:
      return None
   else:
      if n == 0:
         return '0'
      else:
         negative = (n < 0)
         n = abs(n)
         bin_string = ''
         while n != 0:
            if n % 2 == 1:
               bin_string = '1' + bin_string
            else:
               bin_string = '0' + bin_string
            n = n // 2
         if negative:
            bin_string = '-' + bin_string
         return  bin_string 

"""
$test_binary1() tests the binary_string()
with a string. Since n is not an int,
This test is expected to pass returning None 
"""
def test_binary1():
    assert binary_string('hello') == None

"""
$test_binary2() tests the binary_string()
with three 0's. Since it was given an int
but does not pass the first conditional, 
This test is expected to pass returning '0'
"""
def test_binary2():
   assert binary_string(000) == '0'

"""
$test_binary3() tests the binary_string()
with a float. Since a float is not an int,
This test is expected to pass returning None
"""
def test_binary3():
   assert binary_string(7.0) == None

"""
$test_binary4() tests the binary_string()
with an int. Since this int does not equal
0 it continues throughout the function.
This test is expected to pass returning '10000'
"""

def test_binary4():
   assert binary_string(16) == '10000'

