def count_vowels(string):
    """Count the number of vowels in a given string."""
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count += 1
            return count

print(count_vowels('afif'))