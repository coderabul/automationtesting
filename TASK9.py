#2)
arr=[1,2,3,4] 

v=8

x=lambda arr,v: True if v in arr else False

  

if(x(arr,v)): 

  print("Element is Present in the list") 

else: 

  print("Element is Not Present in the list")

#3) 
def fibonacci(count):
  fib_list = [0, 1]
 
  any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, count)))
                                         
 
  return fib_list[:count]

print(fibonacci(10))