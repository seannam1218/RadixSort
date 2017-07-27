from random import randint

ARRAY_LENGTH = 30
NUM_RANGE = 999
randArray = []

def init():
    for i in range(ARRAY_LENGTH):
        randNum = randint(0, NUM_RANGE)
        randArray.append(randNum)
    print(randArray)

def get_digit(number, d):
    return number // 10**d % 10

def countSort(array, digit):
    cArray = [0] * 10
    output = [0] * ARRAY_LENGTH

    # Record the frequency of each value from the input array into the countArray.
    for n in randArray:
        cArray[get_digit(n, digit)] += 1

    # Modify the countArray so that each value of countArray indicates the index of items in output array
    for n in range(9):
        cArray[n+1] = cArray[n] + cArray[n+1]

    # Traverse the input array in reverse order in order to stable sort.
    # countArray now contains the info on the final indices of the numbers that go into the output array.
    # We will be decrementing items in the countArray every time we add the corresponding item from the input array
    # to the output array. This means that when a value repeats, the first to go into the output array should be
    # the last one that appears in the input array, and the earlier items of the same value can go into the output
    # array right before the former (achieved by decrementing the corresponding value from countArray, which represent
    # the index of the output array).
    for item in array[::-1]:
        output[cArray[get_digit(item, digit)]-1] = item
        cArray[get_digit(item, digit)] -= 1

    print(output)
    return output

def radixSort(array, d):
    for i in range(0, d+1):
        array = countSort(array, i)

    return array

init()
sortedArray = radixSort(randArray, 2)
print("Sorted array = " + str(sortedArray))