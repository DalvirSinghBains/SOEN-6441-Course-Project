#L=2R(1-cosA)
# The input values to this function are
# Radius input by the user
# The value of cosA calculated using the Math.sin() function
# The  output value produced is length by the above formula
#degrees=radians*(180/pi)
import math
import AlphaCalculator

class LegthCalculator(object):

  def calculateLength(self):
     #The user is prompted to enter the value of radius at runtime
     print('Enter the value of radius:')
     radius=input()

     #the value of alpha used in the equation is in radians
     #the cosine function included in the Python math library is used for calculating cos(x)
     length= (2.0*radius*(1.0-math.cos(AlphaCalculator.alphaEstimateRadians/2.0)))
     length1 = (2.0 * radius * (1.0 - math.cos(AlphaCalculator.alphaEstimateDegrees/ 2.0)))

     print'The value of length is:'+str(length)+'(alpha in radians)'
     print'The value of length is:'+ str(length1)+'(alpha in degrees)'

def main():
 lengthCalculatorObject=LegthCalculator()
 lengthCalculatorObject.calculateLength()


main()