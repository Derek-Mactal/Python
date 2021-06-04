# 1
for i in range(0,151,1):
    print(i)

#2 Print all multiples of 5 from 5-1000
for i in range(5,1005,5):
    print(i)

#3 Print integers 1-100, if divisible by 5 print coding, if divisible by 10, print coding dojo
for i in range(1,101,1):
    if(i%10 == 0):
        print("Coding Dojo")
    elif(i%5 == 0):
        print("Coding")
    else:
        print(i)


#4 Add odd integers from 0-500,000 print sum
for i in range(0,500000,1):
    sum = 0 
    if(i%2 == 1):
        sum += i
print(sum)

#5 Print positive numbers starting at 2018 decrementing by 4
for i in range(2018,0,-4):
    print(i)

#6 3 vars 
def flexibleCounter(lowNum, highNum, mult):
    for i in range(lowNum,highNum+1,1):
        if(i % mult == 0):
            print(i)

flexibleCounter(2,9,3)