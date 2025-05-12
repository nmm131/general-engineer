# Time: O(a)
def print_all_evens(array):
    for a in array: # O(a)
        if a % 2 == 0:
            print(a)

# Time: O(a) * O(a) = O(a^2)
def print_pairs_with_sum(array, target):
    for a in array: # O(a)
        for b in array: # O(a)
            if a + b == target:
                print(a, b)

# Time: O(a) * O(a - left - 1) = O(a^2)
def print_pairs_with_sum_optimized(array, target):
    for left in range(len(array)): # O(a)
        for right in range(left + 1, len(array)): # O(a - left - 1)
            a = array[left]
            b = array[right]
            if a + b == target:
                print(a, b)

# Time: O(a) * O(k) = O(a * k)
def print_even_sequence(array):
    for a in array: # O(a)
        if a % 2 == 0:
            print("Sequence for {0}".format(a))
            for k in range(0, a): # O(k)
                print(k)

# Time: O(p)
def is_prime(n):
    if  n < 2:
        return False
    for i in range(2, n): # O(p)
        if n % i == 0:
            return False
    return True

# Time: O(a) * O(p)
def print_all_primes(array):
    for k in array: # O(a)
        if is_prime(k): # O(p)
            print(k)

# Time: O(a) + O(a) + O(d) = O(a + d)
# Space: O(d)
def create_table(array):
    min_value = min(array) # O(a)
    max_value = max(array) # O(a)

    table = [0] * (max_value - min_value + 1) # O(d)
    return table

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
    target = 4

    print("Print all evens:")
    print_all_evens(array)

    print("\nPrint pairs with sum:")
    print_pairs_with_sum(array, target)

    print("\nPrint pairs with sum (optimized):")
    print_pairs_with_sum(array, target)

    print("\nPrint even sequence:")
    print_even_sequence(array)
    
    print("\nPrint all primes:")
    print_all_primes(array)

    print("\nCreate table:")
    print(create_table(array))

    print("\nCount pairs which sum to max:")
    print(count_pairs_which_sum_to_max(array))