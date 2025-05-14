# Time: O(a) + O(a) + O(d) = O(a + d)
# Space: O(d)
def create_table(array):
    min_value = min(array) # O(a)
    max_value = max(array) # O(a)

    table = [0] * (max_value - min_value + 1) # O(d)
    return table

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    print("\nCreate table:")
    print(create_table(array))
