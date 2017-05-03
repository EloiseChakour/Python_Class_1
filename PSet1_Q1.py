
#Here, I initialise my variables
sum_of_numbers = 0
i=0

#Using a for loop, I sum the numbers from 1 to 100

for i in range(101):
    sum_of_numbers = sum_of_numbers + i
print("The sum of the numbers from 0 to 100 is %s" %sum_of_numbers)


# Here, I initialize new variables

even_sum = 0
j = 0

# Since 2*50 = 100 we want the next integer since range() is exclusive. Then we sum.

for j in range(51):
    even_sum = 2*j + even_sum
print("The sum of the even numbers from 0 to 100 is %s" %even_sum)

#New variables again ...

odd_sum = 0
k = 0

# Similarly to above, we choose 50 since 2*49+1 = 99 the last odd integer before 100

for k in range(50):
    odd_sum = odd_sum + (2*k + 1)
print("The sum of the odd numbers from 0 to 100 is %s" %odd_sum)

# Sanity check: the sum of the odd integers added to the sum of the even integers should be equal to the sum of all the numbers since there is no other option (unless you consider 0 neither odd nor even but here it is counted as even and if it wasn't it wouldn't contribute to the sum anyway ;) )

total_sum = odd_sum + even_sum
print(total_sum)
