#In this file we write code for find a factorial of a number in python so lets do it

#first we have a take input for find factorail number 
#so using input() function we take input form user 
#since we take input and store into left variable num 
num = input("Enter number :\n")

#and another variable take factorial  and assign value 1 
factorial = 1

#and after that use for loop 
for i in range(1,num+1)
    #Logic of find factorial of number
    factorial= factorial*i
    
#after use logic of factorial num print factorial number
print("Factorial of",num, "is",factorial)
