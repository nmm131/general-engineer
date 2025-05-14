# O(a) + O(a) * O(a) = O(a^2)
def count_pairs_which_sum_to_max(array):
    max_value = max(array) # O(a)
    count = 0

    for left in range(0, len(array)): # O(a)
        for right in range(left + 1, len(array)): # O(a)
            left_value = array[left]
            right_value = array[right]
            if left_value * right_value == max_value:
                count += 1
    return count

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    print("\nCount pairs which sum to max:")
    print(count_pairs_which_sum_to_max(array))