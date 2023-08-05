def ArrangeWithIndex(indexarr,arr):
    newarr = [0]*len(indexarr)
    for i in range(len(arr)):
        newarr[indexarr[i]] = arr[i]
    print(newarr)
if __name__=="__main__":
    ArrangeWithIndex([1, 0, 2],[10, 11, 12])