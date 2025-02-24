

import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    string_new =  s.split(":")
    if (string_new[2]== "AM".lower()):
        if(string_new[0]=="12"):
            return string_new[0] == "00"
        else:
            return s
    if (string_new[2]=="PM".lower()):
        while string_new[0] != "12":
            string_new[0] = str(int(string_new[0]) + 12)
            



        
        
        
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()
