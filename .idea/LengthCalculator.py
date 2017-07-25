#L=2R(1-cosx)
# Radius is input by the user
# The value of cosx in equation [L=2R(1-cosx)] is calculated using the Math.cos(x) function
# The  output value is length by using the above formula
# Two values are length are calculated based on the alpha measurement(radians and degrees)
import math
import AlphaCalculator
from xml.etree.ElementTree import ElementTree,Element, SubElement, Comment, tostring
#import xml.etree.ElementTree as etree

import lxml.etree as etree

def calculateLength():
 #The user is prompted to enter the value of radius at runtime
 user_input=1
 while(user_input==1):

  print('Enter the value of radius:')
  try:
   radius=input()

  except (ValueError, TypeError, NameError):
      print("Oops!  That was no valid number.  Try running the program again...")
      #user_input=1
      break
  if (radius <= 30 and radius>=1):
    # the value of alpha used in the equation is in radians
    # the cosine function included in the Python math library is used for calculating cos(x)
    length_for_radians = (2.0 * radius * (1.0 - math.cos(AlphaCalculator.alphaEstimateRadians / 2.0)))
    length_for_degrees = (2.0 * radius * (1.0 - math.cos(AlphaCalculator.alphaEstimateDegrees / 2.0)))
    print('The value of length is:' + str(length_for_radians) + '(alpha in radians)')
    print('The value of length is:' + str(length_for_degrees) + '(alpha in degrees)')
    print('')

    print('Do you want to calculate for another input radius?')
    print('Enter 1 for Yes')
    print('Enter 2 for No')
    try:
        choice = int(input())
       # break
    except (ValueError,TypeError, NameError):
        print("Oops! the number must be an integer not a character or string or special character")
    if(choice==1):
        user_input=1
    elif(choice==2):
        user_input=0
    else:
        user_input=0
        print("Oops! the choice must be either 1 or 2")
        exit(0)
  else:
     print('Please enter an interger between 1 to 30')
     print('and re-run the program')
     user_input = 0

 print('')
 print('Program has been terminated')
 # try:
#     int(radius)
# except ValueError:
#     try:
#         float(mark)
#     except ValueError:
#         print "This is not a number"
#         user_input = 0



calculateLength()
# def main():
#  #lengthCalculatorObject.calculateLength()
#  user_input=1
#  while user_input==1:
#      print '-------Please select one option:-------'
#      print '1)Press 1 to calculate length!'
#      print '2)Press 2 to save output to XML file!'
#      print '3)Press 3 to view output XML file!'
#      print '4)Press 4 to exit the program!'
#      print('')
#      user_input_second = input()                     #Place input validations or exceptions here
#      if user_input_second == 1:
#          calculateLength()
#      if user_input_second == 2:
#          XMLWriter()
#          print 'Output successfully saved to XML file'
#      if user_input_second == 3:
#          displayXML()
#      if user_input_second == 4:
#          user_input=0
#          print 'You have exited the system'
#          exit(0)
#
# def XMLWriter():
#     top = Element('Cheers')
#     child = SubElement(top, 'Output')
#     child.set('id', '1')
#     radius1 = SubElement(child, 'Radius')
#     radius1.text = radius
#
#     length1 = SubElement(child, 'Length')
#     length1.text = length_for_radians
#
#     # print tostring(top)
#     tree = ElementTree(top)
#
#     tree.write(open(r'C:\Users\DALVIR SINGH BAINS\PycharmProjects\SOEN-6441-Course-Project\.idea\cheers.xml', 'w'))
#     x = etree.parse("cheers.xml")
#     print etree.tostring(x, pretty_print=True)
#
# main()