# Given two sorted and distinct arrays, find the common elements
#
# Example:
# array = [1, 3, 4, 6, 9, 13, 17]
# target = [2, 4, 8, 9, 10, 17, 22, 25, 28]
# Output: [4, 9, 17]

# Time: O(a * t)
def find_common_elems(array, target):
    result = []

    # For each element in the first sorted array
    for a in array: # O(a)
        # Compare it to every element in the second sorted array
        for t in target: # O(t)
            # If a match is found, store it and skip to the next element in the 'array'
            if a == t:
                result.append(a)
                break
    return result

if __name__ == "__main__":
    array = [1, 3, 4, 6, 9, 13, 17]
    target = [2, 4, 8, 9, 10, 17, 22, 25, 28]

    common = find_common_elems(array, target)
    print("Print common elements:")
    print(common)
