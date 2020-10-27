"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
  # user the % or mod opperateor to det if even or odd 
def is_even(n: int) -> bool:
  retrun n % == 0 

def get_middle(input_str):
    # Your code here
    if is_even(len(ipnut_str)):
    # determine if the len of string is even or odd 
    else: 
    #figure out how to get middle chars 
    # return the single middle char if the legnth of the string is odd 
    # return the two middle char is the len is even 
    # calc midpoint index by dividing the len by 2 
    # decimal,  we can roudn the midpoint down
    midpoint = len(input_str) // 2 
    return input_str(midpoint)
    
    
