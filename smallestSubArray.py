# Smallest subarray with sum greater than a given value

def smallestSubArray(x,arr):
    lenArray = []
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum = sum+arr[j]
            if sum > x:
                lenArray.append(len(arr[i:j+1]))
                break
    if(len(lenArray)==0):
        print("Not Possible")
    else:
        print(min(lenArray))

if __name__=="__main__":
    arr = [1, 2, 4]
    x = 8
    smallestSubArray(x,arr)
