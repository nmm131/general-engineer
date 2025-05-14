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

if __name__ == "__main__":
    n = 6

    solutions_optimized = find_solutions_optimized(n)
    print("\nPrint solutions (optimized):")
    print(solutions_optimized)

