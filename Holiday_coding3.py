def maxProfit(A):
    if len(A) <= 1:
        return 0

    min_price = A[0]
    max_profit = 0

    # Iterate through the array starting from the second element
    for price in A[1:]:
        # Update the minimum price if the current price is lower
        min_price = min(min_price, price)
        
        # Update the maximum profit if selling at the current price yields a higher profit
        max_profit = max(max_profit, price - min_price)

    return max_profit
A1 = [1, 2]
output1 = maxProfit(A1)
print("Output 1:", output1)  

# Example 2:
A2 = [1, 4, 5, 2, 4]
output2 = maxProfit(A2)
print("Output 2:", output2)  
