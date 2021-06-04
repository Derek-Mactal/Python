#function that accepts number as input, and counts down to 0
def countDown(num):
    newArr = [] 
    for i in range(num,-1,-1):
        newArr.append(i)
    return newArr
print(countDown(8))

#Function that recieve list with 2 numbers, prints the first and return second
def printAndReturn(list):
    print([list[0]])
    return([list[1]])
print(printAndReturn([5,0]))

#Function that takes list, returns sum of first value + list length

def firstPlusLength(list):
    return(list[0] + len(list))
print(firstPlusLength([1,2,3,4,5,6]))

#function that takes list, creates new list containing values that are greater than its 2nd value
def valuesGreater(list):
    newList = []
    for i in range(0,len(list)-1,1):
        if(list[i] > list[1]):
            newList.append(list[i])
    print(len(newList))
    return(newList)
print(valuesGreater([1,1,3,4,5,1]))

#function takes 2 parameters, makes list, length = size and values = value

def thisThat(size, value):
    newList = []
    for i in range(0,size,1):
        newList.append(value)
    return(newList)
print(thisThat(4,2))