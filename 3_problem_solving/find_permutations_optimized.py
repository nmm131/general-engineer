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
    s = 'abbc'
    b = 'babcabcbebbacbabab'

    permutations_optimized = find_permutations_optimized(s, b)
    print("\nPrint permutations (optimized):")
    print(permutations_optimized)
