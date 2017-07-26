#L=2R(1-cosx)
# Radius is input by the user
# The value of cosx in equation [L=2R(1-cosx)] is calculated using the Math.cos(x) function
# The  output value is length by using the above formula
# Two values are length are calculated based on the alpha measurement(radians and degrees)
import math
import AlphaCalculator
from xml.etree.ElementTree import ElementTree,Element, SubElement, Comment, tostring
import lxml.etree as etree
import xml.etree.cElementTree as ET

class LengthCalculator(object):
    def calculateLength(self):
        #The user is prompted to enter the value of radius at runtime
        user_input=1
        radius_list = []
        length_list = []
        while(user_input==1):
            print('Enter the value of radius:')
            try:
                radius=input()
            except (ValueError, TypeError, NameError):
                print("Oops!  That was no valid number.  Try running the program again with non-character input...")
                #user_input=1
                break
            if (radius <= 30 and radius>=1):
                # the value of alpha used in the equation is in radians
                # the cosine function included in the Python math library is used for calculating cos(x)
                radius_list.append(radius)
                length_for_radians = (2.0 * radius * (1.0 - math.cos(AlphaCalculator.alphaEstimateRadians / 2.0)))
                length_for_degrees = (2.0 * radius * (1.0 - math.cos(AlphaCalculator.alphaEstimateDegrees / 2.0)))
                print('The value of length is:' + str(length_for_radians) + '(alpha in radians)')
                print('The value of length is:' + str(length_for_degrees) + '(alpha in degrees)')
                length_list.append(length_for_radians)
                print('')
                print('Do you want to calculate for another input radius?')
                print('Enter 1 for Yes')
                print('Enter 2 for No')
                print('Enter 3 for viewing XML output')
                try:
                    choice = int(input())
                    # break
                except (ValueError,TypeError, NameError,SyntaxError,UnboundLocalError):
                    print("Oops! the number must be an integer.It must not be a character/string or special character")
                    print("Try re-running the program")
                    exit(0)
                if(choice==1):
                    user_input=1
                elif(choice==2):
                    user_input=0
                elif (choice == 3):
                    #print('Radius values:'+str(radius_list))
                    #print('Length values:'+str(length_list))
                    radius_list_values=radius_list
                    length_list_values = length_list
                    cheers = ET.Element("cheers")
                    for s in range (len(radius_list_values)):
                        for a in range(len(length_list_values)):
                            if(s==a):
                                output = ET.SubElement(cheers, "output")
                                radius = ET.SubElement(output, "radius")
                                radius.text = str(radius_list_values[s])
                                length = ET.SubElement(output, "length")
                                length.text = str(length_list_values[a])
                    tree = ET.ElementTree(cheers)
                    tree.write(open(r'C:\Users\DALVIR SINGH BAINS\PycharmProjects\SOEN-6441-Course-Project\.idea\cheers.xml', 'w'))
                    x = etree.parse("cheers.xml")
                    print etree.tostring(x, pretty_print=True)
                    user_input=0
                else:
                    print("Oops! the choice must be either 1 or 2 or 3")
                    print('Try re-running the program...')
                    #flag=1
                    user_input = 0
            else:
                print('Please enter an interger between 1 to 30')
                print('and re-run the program')
                user_input = 0
        print('')
        print('Program has been terminated')

lengthObject=LengthCalculator()
lengthObject.calculateLength()