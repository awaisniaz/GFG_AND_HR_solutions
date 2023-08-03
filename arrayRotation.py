class ArrayRotation:
    def arrayRotaion(self, arr, d, N):
        print(arr)
        temp = arr[d:N]
        print(temp+arr[0:2])
        print(temp)

    def waveSorting(self, arr):
        arr = sorted(arr)
        n = len(arr)
        print("I am Here")
        print(arr)
        for i in range(n-1):
            print(arr)
            if(arr[i] < arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        print(arr)
