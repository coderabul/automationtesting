# 1.Python program to print odd Numbers in a List
 
# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]
 
only_odd = [num for num in list1 if num % 2 == 1]
odd_count = len(only_odd)
 
print("Even numbers in the list: ", len(list1) - odd_count)
print("Odd numbers in the list: ", odd_count)

#2
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

#3
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
num = 82;    
result = num;    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result);    
     
#Happy number always ends with 1    
if(result == 1):    
    print(str(num) + " is a happy number");    
#Unhappy number ends in a cycle of repeating numbers which contain 4    
elif(result == 4):    
    print(str(num) + " is not a happy number");

#4
print("Enter a Number: ")
num = int(input())

count = 0
while num!=0:
    if count==0: 
        last = num%10
        count = count+1
        rem = num%10
        num = int(num/10)
    sum = rem + last
print("\nSum of first and last digit =", sum)

#6
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size):     
        k = i + 1  
        for j in range(k, _size):   
            if x[i] == x[j] and x[i] not in repeated:   
                repeated.append(x[i])  
    return repeated
#7
def firstNonRepeatingElem(arr, len):
    for i in range(len): #iterates over every element of the array
        for j in range(len): 
            if(arr[i] != arr[j] and i != j):
                return arr[i]  
