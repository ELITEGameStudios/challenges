#Oct 28, 2022
#Noah Simmons

import math

#The given variables
side_1 = 2546375247 
side_2 = 45987482082

#Finds the area through base * height divided by 2
area = (side_1 * side_2) / 2

#Finds the hypotenuse through the pythagorean theorem
hyp = math.sqrt( (side_1 ** 2) + (side_2 ** 2) )

#Finds the perimeter by adding all the sides
perimeter = side_1 + side_2 + hyp

#Prints the final results
print(area)
print(perimeter)
