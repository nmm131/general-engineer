# Given an array, find all pairs that sum to the median value
#
# Example:
# array = [2, 4, 8, 9, 10, 17, 22, 25, 28]
# Output: [(8, 2)]

# Time: O(n^2)
def find_pairs_with_median_sum(array):
    result = []
    n = len(array)

    # Sort the array to ensure the elements are in order
    array.sort() # O(n log n)

    # Calculate the median based on the array length (odd or even number of elements)
    median = array[n // 2] if n % 2 != 0 else (array[n // 2 - 1] + array[n //2]) / 2
    
    # Check all pairs that sum to median
    for i in range(n): # O(n)
        for j in range(i + 1, n): # O(n)
            if array[i] + array[j] == median:
                result.append((array[i], array[j]))
    return result

if __name__ == "__main__":
    array = [2, 4, 8, 9, 10, 17, 22, 25, 28]

    pairs = find_pairs_with_median_sum(array)
    print("\nPrint pairs:")
    print(pairs)

