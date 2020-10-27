"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a: List[int], n: int)->List[int]:
    # Your code here
    # if n is longer then the legnth of the list should return invlaid 
    # we need to return the last n elements as a list of ints

    # we needed to return the first n elements
    #grab everything starting from index 0 to N 
    # we want to grab a subslice where that subslice starts at the beg of our input list and has legnth n 

    # pythons slysting syntax 
    # a[0:n] - get first n elements
    # this says take list a  i want everythign from 0 up to N 
    last_n = a[len(a)-n:]
    retrun last_n

    print(last([1, 2, 3, 4, 5], 1))
    