def count_duplicates(arr):
    counts = {}
    duplicates = {}

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if count > 1:
            duplicates[num] = count

    return duplicates

array_list = [4, 2, 2, 8, 5, 1, 2, 4]
result = count_duplicates(array_list)

for num, count in result.items():
    print(f"{num} = {count}")
