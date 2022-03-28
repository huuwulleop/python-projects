# Find a number in ordered list using binary search

def binary_search(arr, num, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    mid = (low + high) // 2

    if high < low:
        return -1

    if arr[mid] == num:
        return mid
    elif num < arr[mid]:
        return binary_search(arr, num, low, mid - 1)
    else:
        # num > arr[mid]
        return binary_search(arr, num, mid + 1, high)

if __name__ == "__main__":
    arr = [1, 3, 5, 9, 14, 22, 36]
    print(binary_search(arr, 14))
