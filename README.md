RPi README

RPi Scripts:  These are for power cycling a Motorola Cox Cable modem which
randomly loses internet connectivity.  The scripts are run every 10 minutes by
a cron routine in Debian.  The first called is "test_connection.py which sends
a connect request to Microsoft's network connection internet service. 
If an html reply is received then no further action is taken.  If no web
 connection is established then the second script is called.

This script is named "gpiooutput.py".  It sends GPIO pin 11 high and this
signal triggers a relay which cuts the power to the cable modem for
15 seconds, then back on.  4 minutes later "test_connection.py" is called
again, this time by the script, not cron.  If a connection is re established
then the scripts terminate.  If not the power-cycle routine repeats two
more times.  If a connection is not established after three tries, the program 
terminates and does not repeat until the cron function calls it at its 10 min
interval.  Cron executes on boot and every 10 min thereafter until interrupted
from the console or by a shutdown.
The Python scripts are:
test_connection.py
gpiooutput.py
