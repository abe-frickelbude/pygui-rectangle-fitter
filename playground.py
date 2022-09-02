
import fractions
import math
import decimal


# Functions
def print_range(max_value):
    """Print a range of squares from 0 to max_value"""
    for i in range(max_value):
        print('run %d' % i ** 2)


# print_range(5)

# Object metadata and built-ins
print(__file__)
print(print_range.__doc__)
print(print_range.__class__)

# conditions
condition = False  # note the upper-case first letter in True/False
if condition:
    print_range(5)
else:
    print_range(10)

# unicode strings
uc_string = u'Ze qwick bröwn föx'
print(uc_string)

# lists
temp_list = [1, 2, True, False, 'string1', 'string2']
print(temp_list)
# for item in temp_list:
#    print(item)

# WTF?
temp_list += "IXDA"
print(temp_list)

# Slicing (upper bound is exclusive!)
print(temp_list[0:4])

# Tuples - immutable, light-weight version of lists
tuple1 = (1, 2, 3, 4)
tuple2 = ("IX", "DA")
tuple3 = (tuple1, tuple2)

print(tuple1)
print(tuple2)
print(tuple3)

# Repetition in tuples
tuple1 = ('badger ',) * 5
print(tuple1)

# slicing - lower / upper bounds may be omitted
print(tuple1[2:])
print(tuple1[:1])

# Reversing order
tuple2 = (1, 2, 3, 4, 5)
print(tuple2)
print(tuple2[::-1])  # Note the weird-ass syntax in the slice operator here!

# Sets
set1 = {1, 2, 3, 4, 5}
set1.add(6)
print(set1)

print(set1.__contains__(4))
print(7 in set1)  # example of a membership operator
print(12 not in set1)

set2 = frozenset(set1)
print(set2)

# Maps
map1 = {'ix': '1', 'da': '2'}
print(map1)
print(map1['ix'])

print(map1.keys())
print(map1.values())

print(map1.get('a'))

# remove an element
del map1['ix']
print(map1)

# Note: "del" in general seems to deallocate stuff, can also be applied to strings etc.

# strings
string1 = "This is a sample string"
print(string1[6])  # single character
print(string1[4:])  # slice
print(string1[:-4])  # negative index

# Strings are immutable -> statement below won't work!
# string1[6] = "x"

# formatting
# % is is a "string" operator that passes values (for multiple values, use parantheses!)
# to the placeholders inside a string

print("This text contains %d placeholders, %s" % (2, 'yo'))

print("ixda soup".swapcase())
print("ixda soup".title())
print("ixda ixda".count("ixda"))
print("ixda".zfill(10))

long_string = "The quick brown fox jumped over a lazy dog"
print(len(long_string))  # as operator
print(long_string.__len__())  # alternatively as metadata

print(long_string.split())  # split() returns a list of strings, splitting by given separator, default is space)

# Numbers
truncated = int(3.14)
print(truncated)

extended = float(3)
print(extended)

# Note greater control over FP precision is available via the "decimal" module
print(3.14159)
print(decimal.Decimal(3.14159))

# Rational (i.e. fraction) numbers
print(fractions.Fraction(2.5))  # <--- will print as 5/2
print(fractions.Fraction(1, 3))

# produces exactly 7, "*" here is an example of operator overloading by the Fraction class
print(fractions.Fraction(7, 3) * 3)

# Math
print(abs(-10))
print(max(3, 5))
print(math.pi)
print(math.e)  # euler number
print(math.log(256, 2))  # produces log[base2] of 256 = 8

x = 0b00001111
print(type(x))
print(x)

x = 0x80
print(type(x))
print(x)

print(math.modf(math.e))
print(2 ** 10)

