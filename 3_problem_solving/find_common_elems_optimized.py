# Given two sorted and distinct arrays, find the common elements
#
# Example:
# array = [1, 3, 4, 6, 9, 13, 17]
# target = [2, 4, 8, 9, 10, 17, 22, 25, 28]
# Output: [4, 9, 17]

# Time: O(a + t)
def find_common_elems_optimized(array, target):
    # Initialize pointers for both sorted arrays
    i = 0
    j = 0
    result = []

    # Traverse both arrays simultaneously
    while i < len(array) and j < len(target): # O(a + t)
        if array[i] == target[j]:
            # Common element found; add to result
            result.append(array[i])
            i += 1
            j += 1
        elif array[i] < target[j]:
            # Move pointer in 'array' forward
            i += 1
        else:
            # Move pointer in 'target' forward
            j += 1
    return result

if __name__ == "__main__":
    array = [1, 3, 4, 6, 9, 13, 17]
    target = [2, 4, 8, 9, 10, 17, 22, 25, 28]

    common_optimized = find_common_elems_optimized(array, target)
    print("\nPrint common elements (optimized):")
    print(common_optimized)
