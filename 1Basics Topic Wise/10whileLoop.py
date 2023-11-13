
# it is very similar to the for loop, instead of running for the multiple times, it will print only when the condition is true

# we can also use the break and continue keywords in case of requirements

numbers = [9,2,3,5,11,56,2,52,87,39]
l = len(numbers)
i = 0
while i < l:
    print(numbers[i])            # prints entire list, it means we can use the while loop also for iterating the list or tuple 
 
    i +=1


tup = ("chenchu", "rajia", 35, 24, True)
t = len(tup)
j =0
while j < t :                     # prints the entire tuple 
    print(tup[j])
    j +=1



