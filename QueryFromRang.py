def query(l,r,arr):
    print(min(arr[0:r+1]))


if __name__=="__main__":
    arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    l = 4
    r = 7
    query(l,r,arr)