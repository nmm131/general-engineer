# Verification

Your original example is generally not a good test case. Good examples are large, and large test cases take a very long time to run through.

# An efficient verification process

1. Conceptual walk through (FAST!)
2. Hot spots. Where are the high risk lines of code? (FAST!)
    - Math
    - Moving indices
    - Parameters when calling recursion
    - Base cases
    and so on
3. Test cases:
    - Small test cases (MEDIUM)
    - Edge cases (MEDIUM)
        - Boring edge cases
        - Interesting edge cases
    - Big test cases (if you have time) (SLOW)

# Common mistakes
Issue #1:
Verifying algorithm, not code

Issue #2:
Blindly testing, without thinking about what's happening

Issue #3:
Quick, sloppy fixes