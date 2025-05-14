# Given an array, find all pairs that sum to the median value
#
# Example:
# array = [2, 4, 8, 9, 10, 17, 22, 25, 28]
# Output: [(8, 2)]

# Time: O(n log n)
def find_pairs_with_median_sum_optimized(array):
    result = []
    seen = set()
    n = len(array)

    # Sort the array to ensure the elements are in order
    array.sort() # O(n log n)

    # Calculate the median based on the array length (odd or even number of elements)
    median = array[n // 2] if n % 2 != 0 else (array[n // 2 - 1] + array[n //2]) / 2
    
    # Loop through the sorted array
    for num in array: # O(n)
        complement = median - num
        # Check if the complement to the current number exists in the seen set
        if complement in seen:
            result.append((num, complement))
        # Add the current number to the seen set for future complement checks
        seen.add(num)
    return result

if __name__ == "__main__":
    array = [2, 4, 8, 9, 10, 17, 22, 25, 28]
    n = 6

    pairs = find_pairs_with_median_sum_optimized(array)
    print("\nPrint pairs (optimized):")
    print(pairs)