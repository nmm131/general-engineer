# Given an array, for each even number N, generate a 
# list of integers from 0 to N-1 (exclusive of N)
# 
# Example:
# array = [0, 1, 2, 3, 4, 5, 6, 7]
# Output: {
#   {0}: [],
#   {2}: [0, 1]
# ...
# }

# Time: O(a * r)
def find_even_sequence(array):
    result = {}
    for num in array: # O(a)
        if is_even(num):
            sequence = list(range(0, num)) # O(r)
            result[num] = sequence
    return result

# O(1)
def is_even(n):
    if n  % 2 == 0:
        return True
    return False

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    even_sequence = find_even_sequence(array)
    print(even_sequence)