def climbStairs(A):
    if A == 1:
        return 1
    elif A == 2:
        return 2

    ways = [0] * (A + 1)
    ways[1] = 1
    ways[2] = 2

    for i in range(3, A + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[A]

# Example usage:
A1 = 2
A2 = 3

output1 = climbStairs(A1)
output2 = climbStairs(A2)

print("Output 1:", output1)  
print("Output 2:", output2)  
