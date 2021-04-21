def partition(arr, start,end):
    left = start-1
    pivot = arr[end]
    for i in range(start, end+1):
        if(arr[i]<=pivot):
            left+=1
            arr[i],arr[left] =arr[left],arr[i]
    return left

def quickSort(arr, start, end):
    if(start<end):
        pivotPoint = partition(arr, start,end)
        quickSort(arr, start,pivotPoint-1)
        quickSort(arr, pivotPoint+1,end)
        return arr

def missingNumber(arr):
    for i in range(len(arr)-1):
        difference = arr[i+1] - arr[i]
        if(difference > 1):
            for j in range(arr[i]+1,arr[i+1] ):
                print(j)
def main():
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        arr = quickSort(arr, 0, len(arr)-1)

        missingNumber(arr)

main()
