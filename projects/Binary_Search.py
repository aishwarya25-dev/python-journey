#Binary Search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
arr = list(map(int, input("Enter the number separated by comma : ").split(",")))
target = int(input("Enter the number to find : "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element fount at index : {result}")
else:
    print("Element not found!!")
