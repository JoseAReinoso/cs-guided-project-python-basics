"""
Challenge #8:

Create a function that returns the number of arguments it was called with.

Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""

##*data will allow multiple arguments to be passed through just through this simple parameter
def num_args(*data):
    # Your code here
    print(len(data)) 

num_args("foo", "bar")