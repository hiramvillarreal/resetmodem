import urllib2
import gpiooutput
import sys
import os
import logging
import datetime

logging.basicConfig(filename='example.log', level=logging.DEBUG)
retries = 1

def cknet():
    global retries
    debug = 0
    fake_status = 0

    print_debug("Testing for internet connectivity")

    # debugging vv
    if debug == 1:
       print "DEBUG"
       if retries == 1:
           print_debug( "DEBUG succeed case" )
           retries = 0
           return 1
       else:
           print_debug( "DEBUG fail case" )
           return 0
       #return fake_status
     # debugging ^^

    try:
        response=urllib2.urlopen("http://www.msftncsi.com/ncsi.txt")
        print_debug( "Successfully opened URL" )
        return 0
    except urllib2.URLError as err:
        print_debug( "ERROR: Not Connected" )
        gpiooutput.toggle()
        return 1

def print_debug( _string, _print_to_console=1 ):
    if _print_to_console == 1:
        print str( datetime.datetime.now() ) + ":  " + _string
    logging.debug( str( datetime.datetime.now() ) + ": " +  _string )


if __name__ == "__main__":
    send_email = 0

    for i in range(3):
        status = cknet()
        if status == 0:
            print_debug( "Connected" )
            if send_email == 1:
                print_debug( "Detect previous failure, send email with log" )
                os.system('cat example.log | mail -s "sending contents of modemflap.log" efrain.olivares@gmail.com jdhmd@cox.net')
                os.system('mv example.log example.log.bak')
            break

        else:
            print_debug( "Failed Connection, Retrying" )    
            send_email = 1


