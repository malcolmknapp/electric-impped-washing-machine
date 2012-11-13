README

Author: Malcolm Knapp
Date: 11/09/12
Adapterd from code created by

deldrid1
http://forums.electricimp.com/discussion/329/setting-up-a-button-on-hannah/p1

gbsallery
http://forums.electricimp.com/discussion/209/hannah-accelerometer-interrupts/p1

Eric Allan
https://gist.github.com/3894193

colorblink 
http://devwiki.electricimp.com/doku.php?id=colorblink

Description: This code uses the base IOExpander. This code is then extended to add in support for the LED, accelerometer, and buttons. Initialization handled 
by the following variables:

local timeout = 3   // the duration in minutes
local POLL_INTERVAL = 0.5 //  interval is seconds between polling the accelerometer 
local ACCEL_THRESHOLD = 50; // threshold signal for the accelerometer
local INTERNAL_TIMEOUT = timeout*60/POLL_INTERVAL  // scale by poll interval

The values can be adjusted as needed. 

The code logic is as follows

- Power on and the code starts 
- the timeout in minutes in converted to INTERNAL_TIMEOUT which is scaled by the poll interval
- the code waits for a button press
- A button press to starts the monitor and begins measuring the acceleration of the Hannah board.
- the code waits for a acceleration value over the ACCEL_THRESHOLD
- if it see it the code starts a timer that counts up to the timeout value. However if the acceleration goes over ACCEL_THRESHOLD again the timer is reset
- When the timer counts up to the INTERNAL_TIMEOUT the sms is sent and the code waits for another button press. 

This source code under a CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0/) License. You can use, modify, and distribute the source
code and executable programs based on the source code.

However, note the following:

DISCLAIMER OF WARRANTY

This source code is provided "as is" and without warranties as to performance or merchantability. The author and/or distributors of this source code
may have made statements about this source code. Any such statements do not constitute warranties and shall not be relied on by the user in
deciding whether to use this source code.

This source code is provided without any express or implied warranties whatsoever. Because of the diversity of conditions and hardware under 
which this source code may be used, no warranty of fitness for a particular purpose is offered. The user is advised to test the source code 
thoroughly before relying on it. The user must assume the entire risk of using the source code.

Electric Imp, Server, and Twilio Setup

This assumed the Imp you have in already commissioned. If that is not the case please do that first. Also that you are using a Hannah development board with batteries into. Make sure the power selector jumper is set to Batt. 

Setup Your Server
- Make sure the python is installed on the server
- Make sure there is a .local folder. If there is not, create it.
- Add these lines to .bashrc. They will allow python the access the necessary libraries stored in the .local folder 

    export PYTHONPATH=$HOME/.local/lib/python/site-packages:$PYTHONPATH
    export PYTHONPATH=$HOME/.local/lib/python2.6/site-packages:$PYTHONPATH        
    export PATH=$HOME/.local/bin:$PATH

- Install the twilio python module. You can find it and installation instructions at
    
     https://github.com/twilio/twilio-python

Set up the Twilio Adapter
- Create a Twilio Account and mark down your Twilio phone number, account number, and auth token.
- Because this will be a Trial Account you will need to verify your phone number before you can send an SMS to it.
- Replace the Twilio phone number, account number, auto token and the verified phone number placeholders in TwilioAdapater.py with the information from your Twilio account
- The default message is "I am done - The Washing Machine" but you can change it to whatever you want. 
- Copy TwilioAdapter.py onto into the script folder on your server (we used the CGI folder for our project)

Set up Electric Imp Code
- Set up the planner as shown in the Washing Machine Planner.png
- Set up the HTTP Request Node with the the following information
	URL: http://YOUR_SERVER_URL/YOUR_SCRIPT_DIRECTORY/TwilioAdapter.py
	method: POST
	Content Type:  application.x-www-form-urlencoded

	NOTE: this code has NO SECURITY and will run every time the page is loaded so use at your own risk

- Copy Washing Machine V04 into the code section of your account
- Save the code and then upload it to the Imp. This is successful if the LED on the Hannah Board goes red

Usage
- After you load the laundry and start it, press either button on the Hannah. The LED will turn green
- Wait until you get an SMS saying "I am Done - The Washing machine"
- Go get your laundry. The LED will now be red indicating the Imp is in standby mode and ready for the next load. 
- Repeat as necessary. 

