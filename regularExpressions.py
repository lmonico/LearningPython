# Lukas Monico
# 3/18/2021
# Coursera: Using Python to Access Web Data

import re #regx library

#open text file
#create for loop to iterate through each line
#have running sum to "capture" each number
#print results once end of file reached
sum = 0
with open("regex_sum_1041747.txt") as file:
    for line in file:
        matches = re.findall('([0-9]+)', line)
        if(matches != []):
            for num in matches:
                sum = sum + int(num)
print(sum)
