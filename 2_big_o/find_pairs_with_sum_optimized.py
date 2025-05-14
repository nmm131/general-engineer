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

# Time: O(a^2)
def find_pairs_with_sum(array, target_sum):
    result = []

    if len(array) < 2:
        return result
    
    for left in range(len(array)): # O(a)
        for right in range(left + 1, len(array)): # O(a - left - 1)
            left_number = array[left]
            right_number = array[right]
            if sum_matches_target(left_number, right_number, target_sum):
                result.append([left_number, right_number])
    return result

def sum_matches_target(first_number, second_number, target_sum):
    return first_number + second_number == target_sum

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    target_sum = 4
    pairs = find_pairs_with_sum(array, target_sum)
    print(pairs)