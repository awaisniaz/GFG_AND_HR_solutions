# Difference Array | Range update query in O(1)

def query_update(l,r,arr,value):
    for i in range(l,r+1):
        arr[i] = arr[i]+value
    print(arr)


if __name__=="__main__":
    arr = [10, 5, 20, 40]
    l = 0
    r = 1
    query_update(l,r,arr,10)