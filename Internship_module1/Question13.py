def count_pairs(binary):
    count_ones = 0
    total_pairs = 0

    for bit in binary:
        if bit == '1':
            total_pairs += count_ones
            count_ones += 1

    return total_pairs
print(count_pairs(str(input("enter binary string"))))

