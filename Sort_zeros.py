# Sort an array of 0s, 1s and 2s | Dutch National Flag problem

def sortNumbers(arr,n):
    zeros = []
    ones = []
    twos = []
    for i in range(n):
       if arr[i] == 0:
           zeros.append(0)
       if arr[i] == 1:
           ones.append(1)
       if arr[i] == 2:
           twos.append(2)
    print(zeros+ones+twos)
    print(arr)


if __name__=="__main__":
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    n = len(arr)
    sortNumbers(arr,n)