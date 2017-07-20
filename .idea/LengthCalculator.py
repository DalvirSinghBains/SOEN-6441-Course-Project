#L=2R(1-cosA)
# The input values to this function are
# Radius input by the user
# The value of cosA calculated using the Math.sin() function
# The  output value produced is length by the above formula
#degrees=radians*(180/pi)
import math

def lengthCalculator(r):
 print('Enter the value of radius:')
 r=input()
 alpha=2.31
 degrees=alpha*(180/math.pi)
 #print(degrees)
 #print(math.cos(degrees))
 g=math.cos(alpha/2)
 print(g)
 l= 2*r*(1-math.cos(alpha/2))
 print('The value of length is:')
 print(l)
lengthCalculator(2)
