# Given an array, find all even values
#
# Example:
# array = [0, 1, 2, 3, 4, 5, 6, 7]
# Output: [0, 2, 4, 6]

# Time: O(a)
def find_all_evens(array):
    result = []
    for num in array: # O(a)
        if is_even(num):
            result.append(num)
    return result

# Time: O(1)
def is_even(n):
    if n % 2 == 0:
        return True
    return False

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7]
    evens = find_all_evens(array)
    print(evens)