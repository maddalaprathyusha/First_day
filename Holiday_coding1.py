def getRow(k):
    if k == 0:
        return [1]

    row = [1]
    for i in range(1, k + 1):
        next_elem = row[i - 1] * (k - i + 1) // i
        row.append(next_elem)

    return row

# Example usage:
k = 3
result = getRow(k)
print(result)
