
def mergeSort(arr):
    if(len(arr) <= 1):
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge_two_sorted_lists(left,right)

def merge_two_sorted_lists(a,b):
    sorted_list = []
    print(a)
    print(b)
    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i < len_a:
        sorted_list.append(a[i])
        i+=1
    while j < len_b:
        sorted_list.append(b[j])
        j+=1
    return sorted_list

array = [4,87,45,36,100,15,45,98]
print(mergeSort(array))
