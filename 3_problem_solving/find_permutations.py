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

if __name__ == "__main__":
    s = 'abbc'
    b = 'babcabcbebbacbabab'
    permutations = find_permutations(s, b)
    print("\nPrint permutations:")
    print(permutations)
