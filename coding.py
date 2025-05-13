# Given a note (N) and a magazine (M), determine if
# you can build N from the letters in M
#
# Example:
# N = 'this is a ransom note'
# M = 'here is a coding magazine that discusses correctness, readability, maintainability and performance'
# Output: True

# Time: O(n + m)
# Space: O(n + m)
def can_build_ransom_note(n, m):
    note_hash = build_hash_for_note(n)
    magazine_hash = build_hash_for_magazine(m)

    for letter, count in note_hash.items(): # O(n)
        if magazine_hash.get(letter, 0) < count:
            return False
    return True

# Time: O(n)
# Space: O(n)
def build_hash_for_note(n):
    letter_count = {}
    for letter in n: # O(n)
        if letter.isalnum():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

# Time: O(m)
# Space: O(m)
def build_hash_for_magazine(m):
    letter_count = {}
    for letter in m: # O(m)
        if letter.isalnum():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

if __name__ == "__main__":
    n = 'this is a ransom note'
    m = 'here is a coding magazine that discusses correctness, readability, maintainability and performance'

    note = can_build_ransom_note(n, m)
    print(f"Can build ransom note: {note}")