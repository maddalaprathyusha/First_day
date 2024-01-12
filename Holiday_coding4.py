def repeatedAndMissing(A):
    xor_all = 0
    xor_numbers = 0

    for i, num in enumerate(A, start=1):
        xor_numbers ^= i
        xor_all ^= num ^ i

    rightmost_set_bit = xor_all & -xor_all

    missing, repeating = 0, 0

    for i, num in enumerate(A, start=1):
        if i & rightmost_set_bit:
            missing ^= i
        else:
            repeating ^= i

        if num & rightmost_set_bit:
            missing ^= num
        else:
            repeating ^= num

    return [repeating, missing]

# Example usage:
input_array = [3, 1, 2, 5, 3]
output = repeatedAndMissing(input_array)
print("Output:", output)  # Output: [3, 4]
