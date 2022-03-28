# Find a number in ordered list using binary search

def binary_search(arr, num):
    low = 0
    high = len(arr) - 1

    mid = (low + high) // 2
    print(mid)

    if arr[mid] == num:
        return mid
    elif num < arr[mid]:
        print(arr[:mid])
        return binary_search(arr[:mid], num)
    else:
        # num > arr[mid]
        print(arr[(mid + 1):])
        return binary_search(arr[mid:], num)

def main():
    arr = [1, 3, 5, 9, 14, 22, 36]
    arr2 = [14, 22, 36]
    #print(len(arr2) // 2)
    print(binary_search(arr, 14))

main()