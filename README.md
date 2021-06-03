# MerakiGuestPW

## What does this code do

This public repo contains python code that can be used to quickly modify Meraki Guest WiFi PSK passwords


## What does it solve

This code will accept manual or randomly generated passwords to deploy across API enable Meraki enviornments. In addition, it has the ability to deploy as a cron job and/or disply in Webex spaces (using a bot) to diseminate quickly to those who need it.


## Python Environment Setup

It is recommended that this code be used with Python 3.9.x or later.
It is highly recommended to leverage Python Virtual Environments (venv).

Follow these steps to create and activate a venv.
```
# OS X or Linux
virtualenv venv --python=python3.9
source venv/bin/activate
```

## Installation
The MerakiGuestPW.py file should be saved locally.
Also the following python libraries should be installed
```
pip install -r requirements.txt
```

## Variables
This code calls four variables from the Python `os` library
1) `meraki_key` is the Meraki Dashboard API key that can be obtained by following this document
https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API#:~:text=For%20access%20to%20the%20API,to%20generate%20an%20API%20key.
2) `merakinetwork` is the Network Identifier and can be obtained by following this document
https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API
3) `webexBearerToken` is obtained in this document
https://developer.webex.com/docs/api/getting-started
4) `roomID` is the identifier for the created Webex room bot and can be obtained through the Rooms API
https://developer.webex.com/docs/api/v1/rooms

## Creating a Bot
As we are using a Webex bot to post a message about the new SSID password, further documentation on how to create a bot can be found here
https://developer.webex.com/docs/bots

## Example Output
By running this script, you will input variables to allow quick and easy password changes to a Meraki SSID.
Once executed you will deploy the changed PSK password across the enviornment

```
(venv) MerakiGuestPW% python MerakiGuestPW.py --pw Testing123! --ssid 3
Please confirm change to SSID: GuestWiFi with password: Testing123!
Do you want to continue? (Enter y/n)y
Password Modified

OTHER OPTIONS
(venv) MerakiGuestPW% python MerakiGuestPW.py --pw Testing123! --ssid 3 --force
(venv) MerakiGuestPW% python MerakiGuestPW.py --pw Testing123! --ssid 3 --force --webex

FULL HELP SHOWING ALL OPTIONS
(venv) MerakiGuestPW% python MerakiGuestPW.py --help
Usage: MerakiGuestPW.py [OPTIONS]

Options:
  --pw TEXT             Password for SSID - use 'random' to generate 8
                        character password

  --ssid INTEGER        SSID number (0-14)
  --force / --no-force  Continue without y/n verification
  --webex / --no-webex  Send new password to Webex room of your choice
  --help                Show this message and exit.

```

## About Me
I am a Cisco Systems Architect focusing on Automation and Programmability.

**<a href="https://www.linkedin.com/in/patrickrockholz/" rel="nofollow">LinkedIn</a> / <a href="https://twitter.com/patrickrockholz" rel="nofollow">Twitter</a>**
