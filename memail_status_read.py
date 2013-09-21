# memail_status_read.py (0.1)

# September 14, 2013  MODIFIED: September 21, 2013 by JDH. See #'s in script

# Efrain Olivares

# Part of the CMPC project. Using marshal we can store the value of the email flag.
# Similsr to using pickle but faster and avoids having to dreate a hash.
#
# Two scripts: memail_status_set.py and memail_status_read.py.
# Using "memail" to differentiate from "email_" used in the pickle mode.

#!usr/bin/env python

import marshal

inf = open('email_status.dat', 'rb')  # Changed 'datafile.dat' to
                                      #'email_status.dat' when former didn't work.

email_flag = marshal.load(inf)
inf.close
print "marshal returned" +str(email_flag)

# running script returns: marshal returned0

