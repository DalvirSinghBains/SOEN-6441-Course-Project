"""Contains a class called LengthCalculator,a function called calculate_length and imports other modules like xml.etree.elementTree,lxml.etree etc."""
#L=2R(1-cosx)
# Radius is input by the user
# The value of cosx in equation [L=2R(1-cosx)] is calculated using the Math.cos(x) function
# where x is in radians
# The  output value is length by using the above formula
import math

from xml.etree.ElementTree import ElementTree,Element, SubElement,Comment, tostring
import lxml.etree as etree
import xml.etree.cElementTree as ET

import alpha_calculator

class LengthCalculator(object):
    """It calculates the length based on the input radius by the user and generates the XML output.It has a method called called calculate_length that does the whole computation."""

    def calculate_length(self):
        """Get the radius and output the estimated value of length alongwith XML output file"""
        #The user is prompted to enter the value of radius at runtime
        user_input=True #user_input variable controls the outermost while loop
        radius_list = []
        length_list = []
        while(user_input):
            print('Enter the Value of Radius:')
            try:
                radius=input() #user enters the input radius value through text user interface
            except (ValueError, TypeError, NameError,SyntaxError):
                print("Oops!  That was no valid number.  Try running "
                      "the program again with non-character input...")
                break
            if (radius <= 30 and radius >= 1):
                # the value of alpha used in the equation is in radians
                # the cosine function included in the Python math
                # library is used for calculating cos(x)
                radius_list.append(radius) #for dynamic XML output the list of radius values is created
                length_for_radians = (2.0 * radius * (1.0 - math.cos(alpha_calculator.alphaEstimateRadians / 2.0)))
                print('The Value of Length is:' + str(length_for_radians) + ''
                      +'(when alpha is measured in radians)'+''
                      +'[alpha:'+str(alpha_calculator.alphaEstimateRadians)+']')
                length_list.append(length_for_radians) #for dynamic XML output the list of radius values is created
                print('')
                print('Do you want to calculate for another input radius?')
                print('<----Enter 1 for Yes---->')
                print('<----Enter 2 for No----->')
                print('<----Enter 3 for viewing XML output----->')
                try:
                    choice = int(input())
                except (ValueError,TypeError, NameError,SyntaxError,UnboundLocalError):
                    print("Oops! the number must be an integer.It "
                          "must not be a character/string or special character")
                    print("Try re-running the program")
                    exit(0)
                if(choice == 1):
                    user_input=True
                elif(choice == 2):
                    user_input=False
                elif (choice == 3):
                    radius_list_values = radius_list
                    length_list_values = length_list
                    cheers = ET.Element("cheers")     #creation of XML root element "cheers"
                    for s in range (len(radius_list_values)):
                        for a in range(len(length_list_values)):
                            if(s == a):
                                output = ET.SubElement(cheers, "output") #subelements are attached to XML root element
                                radius = ET.SubElement(output, "radius")
                                radius.text = str(radius_list_values[s])
                                length = ET.SubElement(output, "length")
                                length.text = str(length_list_values[a])
                    with open(r'C:\Users\DALVIR SINGH BAINS\PycharmProjects\SOEN-6441-Course-Project\.idea\cheers.xml', 'w') as f:
                        f.write('<?xml version="1.0" encoding="UTF-8" ?>'  #Generation of XML declaration of cheers.xml
                                '<!DOCTYPE cheers [<!ELEMENT cheers (output+)>'
                                '<!ELEMENT output (radius,length)>'
                                '<!ELEMENT radius (#PCDATA)>'
                                '<!ELEMENT length (#PCDATA)>]>')
                        ET.ElementTree(cheers).write(f, 'utf-8')  #cheers.xml file is created that contains output data
                    x = etree.parse("cheers.xml")
                    print etree.tostring(x, pretty_print=True,
                                         xml_declaration=True, standalone=True)
                    user_input=False
                else:
                    print("Oops! the choice must be either 1 or 2 or 3")
                    print('Try re-running the program...')
                    user_input = False
            else:
                print('Please enter an interger between 1 to 30')
                print('and re-run the program')
                user_input = False
        print('')
        print('Program has been terminated')

lengthObject = LengthCalculator()  #Instance of LengthCalculator class is created
lengthObject.calculate_length()