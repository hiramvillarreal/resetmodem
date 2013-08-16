import urllib2
import gpiooutput

def cknet():
    print "Testing for internet connectivity"
    try:
        response=urllib2.urlopen("http://google.com")
        print "Successfully opened URL"
    except urllib2.URLError as err:
        print "We have no connection"
        gpiooutput.toggle()
        pass

if __name__ == "__main__":
    cknet()
