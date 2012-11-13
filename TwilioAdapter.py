#!/usr/bin/python
# adapted from http://jbdeaton.com/2012/send-yourself-an-sms-via-python/

# Name: send-sms-2.py
from twilio.rest import TwilioRestClient
# See: https://github.com/twilio/twilio-python#readme
 
account = "YOUR_TWILIO_ACCOUNT_NUMBER"
token   = "YOUR_TWILIO_AUTH_TOKEN"
client  = TwilioRestClient(account, token)
 
message = client.sms.messages.create(to="+YOUR_VERIFIED_NUMBER", from_="+YOUR_TWILIO_PHONE_NUMBER", body="I am done - The Washing Machine")

print "Content-Type: text/html"
print
import cgi
import cgitb
cgitb.enable()
print """\
<html>
<body>
<h2>Sending SMS!</h2>
</body>
</html>
"""
