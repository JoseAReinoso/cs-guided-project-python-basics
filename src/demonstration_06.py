"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    # Your code here
    txt_lower = txt.lower() #txt.upper() to make it uppercase
    return txt_lower.count('x') == txt_lower.count('o')

def X02(txt):
    #lowercase our txt
    txt_lower = txt.lower()
    x_count = 0
    o_count = 0 
    # loop over each character and coutn x and o
    for character in txt_lower:
        #check if character is x or o
        if character == "x":
            x_count += 1
        elif character == 'o':
            o_count += 1
            
    return  x_count == o_count

              


print(XO("ooxx")) #true
print(XO("xooxx")) #false
print(XO("ooxXm")) #true

print(X02("ooxx")) #true
print(X02("xooxx")) #false
print(X02("ooxXm")) #true


