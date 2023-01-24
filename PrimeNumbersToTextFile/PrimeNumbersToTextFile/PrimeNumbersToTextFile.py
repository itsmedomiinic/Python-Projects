# Program to print all Prime numbers between 1 to 250  

lower = 1
upper = 250

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):  
   # all prime numbers are greater than 1
   if num > 1:  
       for i in range(2, num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 

# Open a file
f = open("prime_numbers.txt", "a")

# Write the prime numbers in a file
for num in range(lower, upper + 1):  
   # all prime numbers are greater than 1
   if num > 1:  
       for i in range(2, num):  
           if (num % i) == 0:  
               break  
       else:  
           f.write(str(num) + "\n")

# Close opened file
f.close()
