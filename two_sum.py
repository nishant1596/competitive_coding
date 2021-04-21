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

def twoSum(arr, requiredSum):
    i=0
    j = len(arr)-1
    while(i<j):
        sum = 0
        sum = arr[i]+arr[j]
        if(sum < requiredSum):
            print('SUM ',sum)
            print('array elements = ',arr[i],arr[j])
            i+=1
        elif(sum>requiredSum):
            print(' SUM ',sum)
            print('array elements = ',arr[i],arr[j])
            j-=1

        elif(sum==requiredSum):
            print(' SUM ',sum)
            print('array elements = ',arr[i],arr[j], ' and their sum is : ',arr[i]+arr[j])
            print([arr[i],arr[j]])
            return
    if(i == j):
        print('-1','-1')


def main():
    t=int(input('enter number of test cases'))
    for i in range(t):
        n = int(input('enter length of array'))
        s = int(input('enter requried sum'))
        arr = list(map(int,input('enter array').split()))
        arr = quickSort(arr, 0, len(arr)-1)
        print(arr)
        twoSum(arr,s)

main()
