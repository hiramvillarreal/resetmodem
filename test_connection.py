import urllib2
import gpiooutput
import sys


retries = 1

def cknet():
    global retries
    debug = 0
    fake_status = 1

    print "Testing for internet connectivity"

    # debugging vv
    if debug == 1:
       print "DEBUG"
       if retries == 1:
           print "DEBUG succeed case"
           retries = 0
           return 1
       else:
           print "DEBUG fail case"
           return 0
       #return fake_status
     # debugging ^^

    try:
        response=urllib2.urlopen("http://www.msftncsi.com/ncsi.txt")
        print "Successfully opened URL"
        return 0
    except urllib2.URLError as err:
        print "We have no connection"
        gpiooutput.toggle()
        return 1


if __name__ == "__main__":
    send_email = 0

    for i in range(3):
        status = cknet()
        print "Toggle Routine"
        if status == 0:
            print "Success"
            if send_email == 1:
                print "Detect previous failure, send email with log"
            break

        else:
            print "Failed to find connection, Retrying"    
            send_email = 1

#    if send_email == 1:
#        print "We would have command to send email here"
