##### Homework 1 #####
##### CNS-380/597 ####
import re

#Write a regular expression to fit the following:

#1 Phone number in the format of
#  xxx-xxx-xxxx
regex1 = '\d{3}\-\d{3}\-\d{4}'


#2 Phone number in the format of
#  (xxx) xxx-xxxx
regex2 = '\(\d{3}\)\s\d{3}\-\d{4}'


#3 Phone number in the format of
#  +x xxx.xxx.xxxx
regex3 = '\+\d\s\d{3}\.\d{3}\.\d{4}'



#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx
regex4 = '\d{3}\-?\d{2}\-?\d{4}'

string = '111-567-9384 (521) 541-5324 +1 341.562.5211 585-12-1211 495182374'

match = re.findall(regex1, string)
if match:
    print('Problem 1')
    print(match)

match = re.findall(regex2, string)
if match:
    print('Problem 2')
    print(match)

match = re.findall(regex3, string)
if match:
    print('Problem 3')
    print(match)

match = re.findall(regex4, string)
if match:
    print('Problem 4')
    print(match)

