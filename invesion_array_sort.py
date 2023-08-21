# Inversion count in Array using Merge Sort

def inversionCount(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[j]<arr[i]):
                count = count+1
    print(count)


if __name__=="__main__":
   inversionCount([1, 20, 6, 4, 5])
