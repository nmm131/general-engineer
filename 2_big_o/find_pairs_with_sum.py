# Given an array and target sum, find all pairs of
# # integers that add up to the target sim
#
# Example:
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# target = 4
# Output: [
#   [0, 4],
#   [1, 3]
# ...
# ]

# O(a^2)
def find_pairs_with_sum(array, target):
    result = []
    for a in array: # O(a)
        for b in array: # O(a)
            if adds_to_sum(a, b, target):
                result.append([a, b])
    return result

# O(1)
def adds_to_sum(num1, num2, target):
    return num1 + num2 == target

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    target = 4
    pairs = find_pairs_with_sum(array, target)
    print(pairs)