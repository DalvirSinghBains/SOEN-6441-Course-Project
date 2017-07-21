#L=2R(1-cosx)
# Radius is input by the user
# The value of cosx in equation [L=2R(1-cosx)] is calculated using the Math.cos(x) function
# The  output value is length by using the above formula
# Two values are length are calculated based on the alpha measurement(radians and degrees)

import math
import AlphaCalculator

class LegthCalculator(object):

  def calculateLength(self):
     #The user is prompted to enter the value of radius at runtime
     print('Enter the value of radius:')
     radius=input()

     #the value of alpha used in the equation is in radians
     #the cosine function included in the Python math library is used for calculating cos(x)
     length_for_radians= (2.0*radius*(1.0-math.cos(AlphaCalculator.alphaEstimateRadians/2.0)))
     length_for_degrees = (2.0 * radius * (1.0 - math.cos(AlphaCalculator.alphaEstimateDegrees/ 2.0)))

     print'The value of length is:'+str(length_for_radians)+'(alpha in radians)'
     print'The value of length is:'+ str(length_for_degrees)+'(alpha in degrees)'

def main():
 lengthCalculatorObject=LegthCalculator()
 #lengthCalculatorObject.calculateLength()
 user_input=1
 while user_input==1:
     print '-------Please select one option:-------'
     print '1)Press 1 to calculate length!'
     print '2)Press 2 to save output to XML file!'
     print '3)Press 3 to view output XML file!'
     print '4)Press 4 to exit the program!'
     print('')
     user_input_second = input()                     #Place input validations or exceptions here
     if user_input_second == 1:
         lengthCalculatorObject.calculateLength()
     if user_input_second == 4:
         user_input=0
         exit(0)
main()