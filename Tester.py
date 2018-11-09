import sys
import getopt
print ("this is the name of the script: ",sys.argv[0])
print ("number of arguments: ",len(sys.argv))
print ("arguments: ",str(sys.argv))

try :
    opts, args = getopt.getopt(sys.argv[1:], "c")
except getopt.GetoptError as err:
        print (err)
