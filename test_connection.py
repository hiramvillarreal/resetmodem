import urllib2
import gpiooutput
import sys
import os
import logging
import datetime

logging.basicConfig(filename='example.log', level=logging.DEBUG)
retries = 1

def cknet():
    """Check Internet Connection
    
    This function is called to probe for an internet connection.  It uses a try/except 
    block to attempt to open a connection to a known stable internet site.  If it succeeds
    it will return false, else if an exception occurs, it will return false.
    
    """
    
    global retries
    debug = 0        # used for debugging only, bypasses internet check
    fake_status = 0  # used for debugging, simulate success or fail for internet check

    print_debug("Testing for internet connectivity")

    # The following block is used for debugging only.
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
    """Add timestamp and write debugging to file.
    
    This function makes use of a timestamp and uses the logging package to write
    to a log.  Wrapping this functionality allows us to change format in one location
    and avoid duplicated code.
    
    """
    
    if _print_to_console == 1:
        print str( datetime.datetime.now() ) + ":  " + _string
    logging.debug( str( datetime.datetime.now() ) + ": " +  _string )


if __name__ == "__main__":
    """Main running loop.
    
    The send_mail flag is set when we do not detect a connection.  Once we have estabished 
    internet connectivity it triggers the email alert.
    
    We loop three times, checking for internet connectivity, exiting on success, or retrying.
    
    This script is set on a cron job which runs every 10 minutes.
    
    """
    
    send_email = 0

    for i in range(3):
        status = cknet()
        if status == 0:
            print_debug( "Connected" )
            if send_email == 1:
                print_debug( "Detect previous failure, send email with log" )
                os.system('tail -n 20 example.log | mail -s "sending contents of modemflap.log" efrain.olivares@gmail.com jdhmd@cox.net')
                os.system('mv example.log example.log.bak')
            break

        else:
            print_debug( "Failed Connection, Retrying" )    
            send_email = 1


