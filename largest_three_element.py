import sys


class ArrayImplementation:

    def secondLargets(self, list):
        second = -sys.maxsize
        first = -sys.maxsize
        for i in range(len(list)):
            if(list[i] > first):

                first = list[i]
            elif(list[i] > second and list[i] < first):

                second = list[i]
        print(second)

    def threeLargestElement(self, list):
        for i in range(len(list)):
            for j in range(len(list)):
                if(list[i] > list[j]):
                    list[i], list[j] = list[j], list[i]
        print(list[0:3])

    def numberSelection(self, list):

        first, second, third = -sys.maxsize
        print(list)
        for i in range(len(list)):
            if(list[i] > first):
                third = second
                second = first
                first = list[i]
            elif(list[i] > second and list[i] != first):
                third = second
                second = list[i]
            elif(list[i] > third and list[i] != second):
                third = list[i]
        print(first, second, third)

    def moveallZero(self, arr):
        count = 0
        for i in range(len(arr)):
            if(arr[i]!= 0):
                arr[count] = arr[i]
                count = count+1
        while count < len(arr):
            arr[count] = 0
            count=count+1
        print(arr)
