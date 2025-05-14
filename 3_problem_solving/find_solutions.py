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

if __name__ == "__main__":
    n = 6

    print("\nPrint solutions:")
    solutions = find_solutions(n)
    print(solutions)
