import math

my_list = [55, 60, 75, 43, 10, 75, 23]
i = 0

average = 0

def Average(input_list):
    my_sum = 0
    length = len(input_list)
    avg = 0
    
    for i in range(length):
        my_sum = my_sum + input_list[i]
        avg = my_sum/length        
    return avg

average = Average(my_list)


def STD(input_list):
    std = 0
    sum_diff = 0
    avg_sum_diff = 0
    length = len(input_list)
    
    for i in range(length):
        sum_diff = sum_diff + (input_list[i]-average)**2
        avg_sum_diff = sum_diff/length
        std = math.sqrt(avg_sum_diff)
    return std
    
standardDeviation = STD(my_list)

print("The average of the list is %s." %average)
print("The standard deviation of the list is %s." %standardDeviation)
