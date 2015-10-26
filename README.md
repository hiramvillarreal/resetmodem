RPi README
==========

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

Installation
============

You will need to install a couple of extenal packages for python and add a cron job to run your scripts.

First install the GPIO basic package onto our pi <reference needed>.

Second, setup smtp on the raspberry py.   There is an easy to follow set of instructions here <URL to instructions>

Once those to packages are installed, you can download this software onto your drive.  
You will install git, then use that to insatll the code as follows:

```
$ sudo apt-get install git
$ sudo apt-get install https://github.com/Niarfe/rpi.git
```

After that you should have directory called rpi, and in it will be the files you'll need.
CD into the directory insure the files are there, gpiooutput, memailstatus, and test_connection are the three main files.
Test_connection is the driver in this case, it's where the action begins and it calls the other files as needed. 

You can set this up on an interval using cron.

```
$crontab -e
Youll see an aditor come up.  At the end of this file add the following line
*/15 * * * * sudo /usr/bin/python /home/pi/rpi/test_connection.py


```

The notation ahead of the script path/name has 5 componentes.  minutes, hours, days, weeks, months.  * means every, and */15 mean every 15 on the hour, or 0, 15, 30, 45.  You can change to every to simpley by changing the first entry to */10.

At every fifteen minutes, the script will run.  If it detectets internet connection, it terminates.  Then at the next 15 minutes it runs again.  If it encouterds a failure, it will log the failure, toggle the power to the modem on and off, then wait a few seconds.  It will repeat the same cycle and try again.  It will give up eventually as the next scycle will take over soom.  In the event it starts working on a retry, then an email will be sent with the log of the last connection activities to the email configured by smtp.

