import pytest
"""
This function accepts any number of arguments.
If at least one argument is provided, all the arguments are integers
and all arguments are either odd or even, the function will return True. 
In any other case, the function will return False
"""

# The *args parameter allows any number/type of argument to be used
def all_odd_or_even(*args):
# checks if there is at least one argument given
    if len(args) < 1:
        return False
    
# Tests if all args are integers using the isinstance() function
    for arg in args:
        if isinstance(arg, int):
            continue
        else:
            return False   
# Tests the elements next to each other to see
# if they are either both even or odd.
# Continue if they are.
# Break loop and return False if they're not.

    counter = 0
    while counter < (len(args) - 1):
        if args[counter] % 2 != 0 and args[counter + 1] % 2 != 0 or args[counter] % 2 == 0 and args[counter + 1] % 2 == 0:
            counter += 1 
            continue
        else:
            return False   
    return True


"""
$test_evenodd1() tests the all_odd_or_even() with 
a float and an int. Because 2.3 is a float and not
and integer, this test is expected to pass and
return False
"""
def test_evenodd1():
    assert all_odd_or_even(2.3,6) == False

"""
$test_evenodd2() tests the all_odd_or_even() with 
a 4 arguments. Because the second argument is a 
string and not an integer, this test is expected
to pass and return False
"""
def test_evenodd2():
   assert all_odd_or_even(4, 'cat', 6, 8) == False


"""
$test_evenodd3() tests the all_odd_or_even() with 
no arguments. Because no arguments were given, this 
test is expected to pass and return False
"""
def test_evenodd3():
   assert all_odd_or_even() == False

"""
$test_evenodd4() tests the all_odd_or_even() with 
4 integers. Because all the integers are even, this 
test is expected to pass and return True.
"""
def test_evenodd4():
   assert all_odd_or_even(4, 12, 18, 1046) == True

"""
$test_evenodd5() tests the all_odd_or_even() with 
4 integers. Because all the integers are odd, this 
test is expected to pass and return True.
"""
def test_evenodd5():
   assert all_odd_or_even(5, 13, 1, 9) == True

"""
$test_evenodd6() tests the all_odd_or_even() with 
4 integers. Because all the integers are not either 
all even or all odd, the test is expected to pass 
and return False
"""
def test_evenodd6():
   assert all_odd_or_even(4, 0, 3, 1046) == False

"""
$test_evenodd7() tests the all_odd_or_even() with 
2 lists. Because they are not integers, this test
is expected to pass and return False
"""
def test_evenodd7():
   assert all_odd_or_even(['hello'], [5]) == False

"""
$test_evenodd8() tests the all_odd_or_even() with 
4 negative integers. Though the integers are not 
positive, they are all even. the test should pass
and return true
"""
def test_evenodd8():
   assert all_odd_or_even(-2, -4, -6, -8) == True