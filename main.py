from largest_three_element import ArrayImplementation
from arrayRotation import ArrayRotation


if __name__ == "__main__":
    arr = ArrayImplementation()
    ar = ArrayRotation()

    list = [10, 4, 3, 50, 23, 90]
    N = len(list)
    arr.threeLargestElement(list)
    arr.secondLargets([12, 35, 1, 10, 34, 1])
    arr.moveallZero([1, 2, 0, 4, 3, 0, 5, 0])
    arr.segregateEvenOdd([7, 2, 9, 4, 6, 1, 3, 8, 5],
                         len([7, 2, 9, 4, 6, 1, 3, 8, 5]))
    
    ar.arrayRotaion(list,2,N)
    ar.waveSorting([10, 4, 3, 50, 23, 90])
