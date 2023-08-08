def smallestMissing(arr):
    new = sorted(arr)
    minimum = -1
    for i in range(len(new)):
        if i != new[i]:
            minimum = i
            break
    print(minimum)


if __name__=="__main__":
    smallestMissing([0, 1, 2, 3, 4, 5, 6, 7, 10])