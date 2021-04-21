# Here we are using quick sort to sort both the string after converting them to List, then comparing them in single iteration because they are already sorted, 
# so, if any of the character doesn't match, we just return False and print 'NO'

def partition(arr,start,end):
    pivot = arr[end]
    left = start-1
    for i in range(start, end+1):
        if(arr[i] <= pivot):
            left+=1
            arr[i],arr[left] = arr[left],arr[i]

    return left

def sort(arr, start, end):
    if(start<end):
        pivotPosition = partition(arr, start,end)
        sort(arr, start,pivotPosition-1)
        sort(arr, pivotPosition+1, end)
        return arr


def compareArray(arr1,arr2):
    i = 0
    counter = 0
    while(i<len(arr1) and i < len(arr2)):
        if(arr1[i] == arr2[i]):
            counter+=1
        else:
            return False
        i+=1
    if(counter == len(arr1) and counter == len(arr2)):
        return True
    else:
        print('NO')
        return False

def main():
    t=int(input())
    for i in range(t):
        n = int(input())
        str1 = list(map(str, input()))
        str2 = list(map(str, input()))

        str1 = sort(str1, 0, len(str1)-1)
        str2 = sort(str2,0, len(str2)-1)

        result = compareArray(str1,str2)
        if(result == True):
            print('YES')
        else:
            print('NO')


main()
