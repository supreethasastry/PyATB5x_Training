# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Anwser

def first_non_repeating(string):

    seen = set()  # To track characters seen more than once

    unique = []   # To track characters in the order they appear

    for char in string:

        if char in seen:

            continue  # Skip if already seen

        if char in unique:

            unique.remove(char)  # Move to seen if repeated

            seen.add(char)

        else:

            unique.append(char)  # Add to unique if seen first time

    # The first character in the unique list is the non-repeating one

    return unique[0] if unique else None

# Test Cases

print(first_non_repeating("swiss"))  # Output: 'w'

print(first_non_repeating("aabbcc"))  # Output: None

print(first_non_repeating("alphabet"))  # Output: 'l'