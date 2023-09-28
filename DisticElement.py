def DisticElemen(arr): 
    newarr = []
    for i in range(len(arr)):
        if(i == arr.index(arr[i])):
            newarr.append(arr[i])
    print(newarr)
DisticElemen([1, 2, 3, 4, 5])
