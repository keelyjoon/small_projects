import pytest

def independent(list_a, list_b):
   '''
      We can say that two lists are independent if no value occupies the
      same position in both lists.  Independent lists are not
      required to have the same length.

         For example, [1,2] and [2,1,3] are independent, and
         [1,2,3]  and [4,2,'a'] are not independent.
         
      Parameters:
         list_a and list_b must be lists

      Returns True if list_a and list_b are independent, and
      returns False if they are not
   '''
   if type(list_a) is not list  or type(list_b) is not list:
      return False
   else:
      min_length = min(len(list_a), len(list_b))
      for i in range(min_length):
         if list_a[i] == list_b[i]:
            return False
      return True

"""
$test_independent1() tests the independent()
with two lists of different lengths containing ints.
This test is expected to pass returning True
"""
def test_independent1():
    assert independent([1,2],[2,1,3]) == True

"""
$test_independent2() tests the independent()
with two lists containing strings. Since the
first index is the same value in both lists,
This test is expected to pass returning False
"""
def test_independent2():
   assert independent(['a','b','c'],['f','b','g']) == False

"""
$test_independent3() tests the independent()
with two empty lists. Because there is nothing 
to compare in these lists,
The test is expected to pass returning True
"""
def test_independent3():
   assert independent([],[]) == True

"""
$test_independent4() tests the independent()
with two lists of strings. In the first list, 
the string is written using a double quote. In
the second list, the strings are written using 
single quotes. Because the strings in index 0
are the same,
This test is expected to fail returning False 
"""
def test_independent4():
   assert independent(["hello"],['hello','world']) == False

"""
$test_independent5() tests the independent()
with two lists of ints. The lists contains 
the same numbers with negative and positive 
values. Because no corresponding index has
the same value,
The test is expected to pass returning True
"""
def test_independent5():
   assert independent([1, 2 , 3],[-1, -2, -3]) == True