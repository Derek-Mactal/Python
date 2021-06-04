#given list, function that changes all positive numbers = "big"
def biggie_size(list):
    for i in range(0,len(list)-1,1):
        if(list[i] < 0):
            list[i] = "big"
    return(list)
print(biggie_size([-3,-3,-3,0]))

#given list, function that replace last value with number of positive values
def count_positives(list):
    count = 0
    for i in range(0,len(list)-1,1):
        if(list[i] > 0):
            count += 1
    list[len(list)-1] = count
    return(list)
print(count_positives([1,2,-1,0]))

#function that takes list, returns sum of all values

def sum_total(list):
    sum = 0
    for i in range(0,len(list)-1, 1):
        sum += list[i]
    return(sum)
print(sum_total([2,2,2,2]))

#Function that takes list, returns average
def average(list):
    sum = 0
    for i in range(0,len(list)-1,1):
        sum += list[i]
    return(sum/len(list))
print("Average is", average([5,4,2,6]))

#function that takes list and returns length

def length(list):
    return(len(list))
print("The length of list is..", length([1,2,3,4,5]))

#6 function that takes list and returns minimum value, if list empty return false

def minimum(list):
    for i in range(0,len(list)-1,1):
        if(len(list) == 0):
            return("False")
        elif(list[0] > list[i]):
            list[0] = list[i]
    return(list[0])
print("minimum is...", minimum([]))

#7
def maximum(list):
    for i in range(0,len(list)-1,1):
        if(len(list) == 0):
            return("False")
        elif(list[0] < list[i]):
            list[0] = list[i]
    return(list[0])
print("maximum is...", maximum([1,3,0,2]))

#8 function that takes listm returns dictionary that has sumtotal average, minumum, maximum, length 
def ultimate(list):
    sumTotal = 0
    minimum = 0
    maximum = 0
    #library = {'Sum':sumTotal, 'average': (sumTotal / len(list)), 'minimum': minimum, 'maximum': maximum,'length':len(list)}
    for i in range(0,len(list),1):
        sumTotal += list[i]
        if(list[0] > list[i]):
            list[0] = list[i]
            minimum = list[0]

        if(list[0] < list[i]):
            list[0] = list[i]
            maximum = list[0]
    return {'Sum':sumTotal, 'average': (sumTotal / len(list)), 'minimum': minimum, 'maximum': maximum,'length':len(list)}
print(ultimate([76,2,-1,0,6]))


def reverse_list(list): 
    temp = 0
    for i in range(0,int(len(list)/2),1):
        temp = list[len(list)-1-i]
        list[len(list)-1-i] = list[0+i] 
        list[0+i] = temp
        print(list)
    return list
print(reverse_list([1,2,3,4,5]))

