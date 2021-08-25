
# imports
import sys
import os
from time import sleep
import getpass
import turtle as t

# Copyright info
copyright = "X Language is free software by Xchuang 2021. All rights reserved.\nCode help by Xchuang Software helper."
# End Copyright info

# Variables
IntV = []
StrV = {}
BoolV = {}
CodeTips = "\>: "
SkmbolKeys = ('/', '?', '/', '$', '`')
err = 'Error message:'
# End Variables

# main code

# defs
# Identification code
def main():
    print('XL', sys.path[0]+'>', '& This')

if __name__ == "__main__":
    main()

def IC(code):
    # Quit
    if code == "quit":
        return 0
    # End Quit

    # Log
    elif code[0: 3] == 'log':
        print(code[4:])
    # End Log

    # Give V
    elif code[0: 3] == 'var':
        if code[4: 7] == 'int':
            IntV.append(code[8:])
            print('Saved', code[8:], 'as int', IntV.index(code[8:]))
    # End Give V

    # Get v
    elif code[0: 3] == 'get':
        if code[4: 7] == 'int':
            if code[8:] != '':
                if (0 <= int(code[8:])) and (int(code[8:]) < len(IntV)):
                    print(IntV[int(code[8:])])
                else:
                    print(err, "No variable named:", code[4:])
            else:
                print(err, "input the index after 'get int > [] < '")
    # End Get V

    # Err
    elif code == 'err':
        print(err, "Unknow error")
        return 0
    # End Err

    # Ai
    elif code[0:2] == 'ai':
        print('started ai')
        print('Hi', getpass.getuser(), ', I am Xabrina')
        xai = 'Xabrina: '
        userai = getpass.getuser() + ': '
        while True:
            aicvzs = input(userai)
            if 'bye' in aicvzs or 'see you' in aicvzs:
                print(xai + 'bye, see you next time.')
                break
            elif 'draw' in aicvzs:
                if 'circle' in aicvzs:
                    t.pensize(6)
                    t.circle(80)
                    print('That is a good circle q(≧▽≦ q)')
                elif 'sqare' in aicvzs:
                    t.pensize(4)
                    t.forward(40)
                    t.left(90)
                    t.forward(40)
                    t.left(90)
                    t.forward(40)
                    t.left(90)
                    t.forward(40)
                    t.left(90)
                    t.forward(40)
                    print('That is a well sqare q(≧▽≦ q)')
                else:
                    print('What do you want to draw (⊙ o⊙ )?')
            else:
                print("ummm...I don't know what you are saying")
    # End Ai

    # Unknow Code
    else:
        print("Unknow Code '" + code + "' :</")

    print("")
# End defs
# End Identification code

# PS C:\Users\yeli>


# print copyright info


sleep(0.5)

for i in range(len(copyright)):
    print(copyright[i], end="")

for i in range(2):
    print("")
# End print copyright info

sleep(0.5)

# Input Code
while True:
    if IC(input(CodeTips)) == 0:
        break
# End Input Code
# End main code
