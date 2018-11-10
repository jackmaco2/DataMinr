'''
MetaJack Tools
By Jack Countryman & Nate Wilwerding
'''

import sys
import subprocess
import getopt

def useage() :
    print ("DataMinr by Metajack")
    print ("\n")
    print ("Usage: dataminr.py -n target_name [modifiers]")
    print ("-n --name            -target name")
    print ("-c --city            -city of residence")
    print ("-S --State           -state of residence")
    print ("-s --school          -current or alma mater")
    print ("-w --workplace       -current or former place of employment")
    print ("-a --age             -target's age")
    print ("-A --AgeRange        -takes in age range \"[low]-[high]\"")
    print ("-b --birthday        -target's birthday [MM/DD/YYYY]")
    print ("-g --gender          -target's gender [M or F]")
    print ("-h --hometown        -where the user is from originally")
    print ("\n")
    print ("Examples:")
    print ("dataminr.py -c chicago -S Chicago -s University of Chicago -w Hayneedle")
    from random import randint
    value = randint(1, 3)
    strang = "none"
    if (value == 1) :
            strang = "I'm not dumb. I just have a command of thoroughly useless information.\n\t\t\t -Bill Watterson"
    if (value == 2) :
            strang = "Withholding information is the essence of tyranny. Control of the flow of information is the tool of the dictatorship.\n\t\t\t -Bruce Coville"
    if (value == 3) :
            strang = "Opinion is usually something which people have when they lack comprehensive information\n\t\t\t -Idries Shah"
    if (value == 4) :
            strang = "We're all living in each other's paranoia.\n\t\t\t -Elliot Alderson"
    print ("\n" + strang)
    sys.exit(0)

def main() :
    global input
    global name
    global city
    global state
    global school
    global workplace
    global age
    global AgeRange
    global birthday
    global gender
    global hometown

    useage()


main() 
