def find_smallest_and_largest(numbers):
    if not numbers:
        raise ValueError("The array is empty.")
    
    smallest = largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest

numbers_list = [4, 2, 8, 5, 1]
smallest_num, largest_num = find_smallest_and_largest(numbers_list)

print("Smallest number =", smallest_num)
print("Largest number =", largest_num)
