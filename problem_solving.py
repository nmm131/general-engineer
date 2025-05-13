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

# Given an integer N, find all solutions to the equation a^3 + b^3 = c^3 + d^3
# where a, b, c and d are ints between 1 and N
#
# Example:
# n = 6
# Output = [
#   (1, 12, 9, 10),
#   (2, 16, 12, 14)
# ...
# ]

# Time: O(n^4)
def find_solutions(n):
    results = []

    # Loop over all possible values of a, b, c and d
    for a in range(1, n + 1): # O(n)
        for b in range(1, n + 1): # O(n)
            for c in range(1, n + 1): #O(n)
                for d in range(1, n + 1): #O(n)
                    # Check if sum of cubes for a and b equals the sum of cubes for c and d
                    if a**3 + b**3 == c**3 + d**3:
                        # If the equation holds true, append the solution to the results list
                        results.append((a, b, c, d))
    return results

# Time: O(n^2) or O(n^4) worse case
# Space: O(n^2)
def find_solutions_optimized(n):
    results = []
    sum_dict = {}

    # Precompute all possible sums a^3 + b^3 and store them in a dictionary
    for a in range(1, n + 1): # O(n)
        for b in range(1, n + 1): # O(n)
            sum_val = a**3 + b**3

            # Store the pair (a, b) that produces the sum in the dictionary
            if sum_val in sum_dict:
                sum_dict[sum_val].append((a, b))
            else:
                sum_dict[sum_val] = [(a, b)]

    # For each pair of (c, d), check if the sum c^3 + d^3 exists in the dictionary
    for c in range(1, n + 1): # O(n)
        for d in range(1, n + 1): # O(n)
            sum_val = c**3 + d**3

            # If the sum exists in the dictionary, append all the matching pairs
            if sum_val in sum_dict:
                for (a, b) in sum_dict[sum_val]:
                    results.append((a, b, c, d))
    return results

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

# Given two strings, S and B, find all permutations of S within B
#
# Example:
# S = abbc
# B = babcabcbebbacbabab
# Output: [
#   'babc',
#   'bcab'
# ...
# ]

# Time: O(b * s)
# Space: O(s + b)
def find_permutations(s, b):
    result = []
    s_len = len(s)
    b_len = len(b)
    s_freq = {}

    if s_len > b_len:
        return result
    
    # Create frequency count for string s
    for char in s: # O(s)
        if char in s_freq:
            s_freq[char] += 1
        else:
            s_freq[char] = 1

    # Sliding windows approach over b
    for i in range(b_len - s_len + 1): # O(b)
        window = b[i:i + s_len] # O(s)

        # Create a window frequency count for the current window
        window_freq = {}
        for char in window: # O(s)
            if char in window_freq:
                window_freq[char] += 1
            else:
                window_freq[char] = 1

        # Compare the frequency counts of the window and s
        if window_freq == s_freq: # O(s)
            result.append(window)
    return result

# Time: O(b)
# Space: O(s + b)
def find_permutations_optimized(s, b):
    result = []
    s_len = len(s)
    b_len = len(b)
    s_freq = {}

    if s_len > b_len:
        return result
    
    # Create frequency count for string s
    for char in s: # O(s)
        if char in s_freq:
            s_freq[char] += 1
        else:
            s_freq[char] = 1

    # Create a window frequency count for the current window
    window_freq = {}
    for i in range(s_len): # O(s)
        char = b[i]
        if char in window_freq:
            window_freq[char] += 1
        else:
            window_freq[char] = 1

    # Check if the initial window is a valid permutation
    if window_freq == s_freq:
        result.append(b[:s_len])

    # Sliding window over the rest of string b
    for i in range(s_len, b_len): # O(b - s)
        # Add the new character in the window
        new_char = b[i]
        if new_char in window_freq:
            window_freq[new_char] += 1
        else:
            window_freq[new_char] = 1
        
        # Remove the old character from the window
        old_char = b[i - s_len]
        window_freq[old_char] -= 1
        if window_freq[old_char] == 0:
            del window_freq[old_char]
        
        # Compare window to s_freq
        if window_freq == s_freq:
            result.append(b[i - s_len + 1:i + 1])
    return result

if __name__ == "__main__":
    array = [1, 3, 4, 6, 9, 13, 17]
    target = [2, 4, 8, 9, 10, 17, 22, 25, 28]
    n = 6

    common = find_common_elems(array, target)
    print("Print common elements:")
    print(common)

    common_optimized = find_common_elems_optimized(array, target)
    print("\nPrint common elements (optimized):")
    print(common_optimized)

    print("\nPrint solutions:")
    solutions = find_solutions(n)
    print(solutions)

    solutions_optimized = find_solutions_optimized(n)
    print("\nPrint solutions (optimized):")
    print(solutions_optimized)

    pairs = find_pairs_with_median_sum(target)
    print("\nPrint pairs:")
    print(pairs)

    pairs = find_pairs_with_median_sum_optimized(target)
    print("\nPrint pairs (optimized):")
    print(pairs)

    s = 'abbc'
    b = 'babcabcbebbacbabab'
    permutations = find_permutations(s, b)
    print("\nPrint permutations:")
    print(permutations)

    permutations_optimized = find_permutations_optimized(s, b)
    print("\nPrint permutations (optimized):")
    print(permutations_optimized)
