def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    num=0
    while num<len(lst):

        if lst[num] < 0:
            return lst[num]
        num+=1
    return "No negatives"



# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
find_first_negative([3, 5, -1, 7, -2, 8])
find_first_negative([2, 10, 7, 0])