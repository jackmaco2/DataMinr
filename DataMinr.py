#MetaJack Tools
#By Jack Countryman
#

def useage() :
    print "DataMinr by Metajack"
    print
    print "Usage: dataminr.py -n target_name [modifiers]"
    print "-c --city            -city of residence"
    print "-S --State           -state of residence"
    print "-s --school          -current or alma mater"
    print "-w --workplace       -current or former place of employment"
    print
    print
    print "Examples:"
    print "dataminr.py -c chicago -S Chicago -s University of Chicago -w Hayneedle"
    from random import seed
    from random import randint
    seed (1)
    for _ in range(10):
        value = randint(0, 10)
        print(value)
    print ""