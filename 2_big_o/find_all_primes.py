# Given an array, find all prime numbers
#
# Example:
# array = [0, 1, 2, 3, 4, 5, 6, 7]
# Output: [1, 2, 3, 4, 7]

# O(a * p)
def find_all_primes(array):
    result = []
    for num in array: # O(a)
        if is_prime(num): # O(p)
            result.append(num)
    return result

# O(p)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n): # O(p)
        if n % i == 0:
            return False
    return True
    

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7]
    primes = find_all_primes(array)
    print(primes)