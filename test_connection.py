import urllib2


def cknet():
    print "cknet"
    try:
        response=urllib2.urlopen("http://google.com")
        print "we have a connection"
    except urllib2.URLError as err: pass
    print "We have no connection"

if __name__ == "__main__":
    cknet
