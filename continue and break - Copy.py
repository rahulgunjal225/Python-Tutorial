def find_product(num1, num2, num3):
    nums = [num1, num2, num3]

    # Check if 7 is in the list
    if 7 in nums:
        index_7 = nums.index(7)
        # Values to consider are only to the right of 7
        values_to_multiply = nums[index_7 + 1:]

        # If no values to multiply, return -1
        if len(values_to_multiply) == 0:
            return -1
        
        # If only one value to multiply, return that value
        if len(values_to_multiply) == 1:
            return values_to_multiply[0]

        # Else calculate product of values to the right
        product = 1
        for val in values_to_multiply:
            product *= val
        return product
    else:
        # If no 7, product of all three
        product = 1
        for val in nums:
            product *= val
        return product


# Test cases from sample inputs and one extra
print(find_product(1, 5, 3))  # Expected output: 15
print(find_product(3, 7, 8))  # Expected_
