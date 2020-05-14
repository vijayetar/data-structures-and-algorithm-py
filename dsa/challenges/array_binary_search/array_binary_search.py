def BinarySearch(arr, el):
    l = 0
    h = len(arr)-1

    if el not in arr:
        return -1
    elif el == arr[0]:
        return 0
    elif el == arr[h]:
        return h

    while arr[l] != arr[h]:
        m = (h+l)//2
        if arr[m]==el:
            return m
        elif arr[m]>el:
            h=m
        elif arr[m]<el:
            l=m+1

def for_loop_search(arr,el):
    if el not in arr:
        return -1
    elif el == arr[0]:
        return 0
    elif el == arr[len(arr)-1]:
        return len(arr)-1
    for i in range(len(arr)):
        if arr[i] == el:
            return i

def quick_method_search(arr,el):
    if el not in arr:
        return -1
    return arr.index(el)
