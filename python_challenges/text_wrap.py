'''You are given a string S and width w. 
Your task is to wrap the string into a paragraph of width w.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''

import textwrap

def wrap(string, max_width):
    return '\n'.join([string[i:i+max_width] for i in range(0, len(string), max_width)])

