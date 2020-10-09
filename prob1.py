def sumNum(num):
    previousN = 0
    for i in range(num):
        sum = previousN + i 
        print("corent number is : ",i , "previous number is ",previousN, "sum is " ,sum)
        previousN = i 
    
sumNum(10)
