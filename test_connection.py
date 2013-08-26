import urllib2
import gpiooutput
import sys
def cknet():
    print "Testing for internet connectivity"
    try:
        response=urllib2.urlopen("http://www.msftncsi.com/ncsi.txt")
        print "Successfully opened URL"
        return 0
    except urllib2.URLError as err:
        print "We have no connection"
        gpiooutput.toggle()
        return 1
if __name__ == "__main__":
    for i in range(3):
        print "Toggle Routine"
        if 0 == cknet():
            print "Success"
            sys.exit()

    
    
