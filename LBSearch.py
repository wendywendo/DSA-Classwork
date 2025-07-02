# Linear search
'''

numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

key_value = 88
found = False

for i in numbers:
    if i == key_value:
        found = True
        break


if found is True:
    print(f"Element {key_value} Found!")

else:
    print(f"Element {key_value} Not Found!")

'''

# Binary search

numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

def binary_search(numbers, key_value):
    start_index = 0
    end_index = len(numbers) - 1

    while start_index <= end_index:
        mid = (start_index + end_index) // 2

        mid_val = numbers[mid]

        if mid_val == key_value:
            return mid
        elif mid_val < key_value:
            start_index = mid + 1
        elif mid_val > key_value:
            end_index = mid - 1

    return -1

def recursive_binary_search(arr, target, start_index, end_index):
    if start_index > end_index:
        return  -1

    mid = (start_index + end_index) // 2
    mid_val = arr[mid]

    if mid_val == target:
        return mid
    elif mid_val < target:
        return recursive_binary_search(arr, target, mid + 1, end_index)
    else:
        return recursive_binary_search(arr, target, start_index, mid - 1)


if __name__ == "__main__":
    key_value = 88

    print(f"Element {key_value} found at pos {binary_search(numbers, key_value)}")