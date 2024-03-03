#ex1
def multiply(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total
print(multiply((8, 2, 3, -1, 7))) 
#ex2
def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print(s)
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    print("No. of Lower case Characters: ", d["LOWER_CASE"])
string_test('The quick Brown Fox') 
#ex3
def Palindrome(string):
    left_pos = 0
    right_pos = len(string) - 1
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True
print(Palindrome('aasaa')) 
#ex4
import time
import math
def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = math.sqrt(number)
    print(result)
number = 25100
milliseconds = 2123
square_root_after_milliseconds(number, milliseconds)
#ex5
x = (True, True, True)
result = all(x)
print(result)