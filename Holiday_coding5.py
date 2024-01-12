def distributeCandy(A):
    n = len(A)
    candies = [1] * n

    # Traverse from left to right
    for i in range(1, n):
        if A[i] > A[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Traverse from right to left and update candies array
    for i in range(n - 2, -1, -1):
        if A[i] > A[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Return the total minimum candies needed
    return sum(candies)

# Example usage:
input_array = [1, 2]
output = distributeCandy(input_array)
print("Output:", output)  # Output: 3
