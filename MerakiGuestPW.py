#!/usr/local/bin/python3
import requests
import json
import os
import click
import random
import string
import sys

meraki_key = os.environ.get('MERAKI_API_KEY')
merakinetwork = os.environ.get('MY_MERAKI_NETWORK')
webexBearerToken = os.environ.get('WEBEX_BEARER_TOKEN')
roomID = os.environ.get('WEBEX_PAROCKHO_BOT')

baseurl = "https://dashboard.meraki.com/api/v1/networks/"

def randomize_pw():
    pw_chars = string.ascii_letters + string.digits
    pw = ''.join(random.choice(pw_chars) for i in range(8))
    return pw

@click.command()
@click.option('--pw', type=str, default='', help="Password for SSID - use 'random' to generate 8 character password")
@click.option('--ssid', type=int, default=14, help="SSID number (0-14)")
@click.option('--force/--no-force', default=False, help="Continue without y/n verification")
@click.option('--webex/--no-webex', default=False, help="Send new password to Webex room of your choice")
def changePass(pw, ssid, force, webex):
    if pw == 'random':
        pw = randomize_pw()
    url = baseurl + str(merakinetwork) + '/wireless/ssids/'
    payload = json.dumps(
    {"psk": pw
    })
    headers = {
    'X-Cisco-Meraki-API-Key': meraki_key,
    'Content-Type': 'application/json'
    }
    response_get = requests.get(url + str(ssid), headers=headers)
    data = response_get.json()
    
    if force:
        response = requests.request("PUT", url + str(ssid), headers=headers, data=payload)
    else:   
        print(f'Please confirm change to SSID: {data["name"]} with password: {pw}')
        while (answer := input("Do you want to continue? (Enter y/n)").lower() ) not in {"y", "n"}: 
            pass
        if answer == 'y':
            response = requests.request("PUT", url + str(ssid), headers=headers, data=payload)
            # print(response.status_code)
            if response.status_code == 200:
                click.echo('Password Modified')
        if answer == 'n':
            sys.exit(0)

    #Post in Webex using '--webex' option
    if webex:
        #get SSID and password and set it to the 'message' variable
        message = f'The new password for SSID {data["name"]} is {pw}'
        #set the 'url' variable to the webex url
        url = "https://api.ciscospark.com/v1/messages"
        #define body and header data
        payload="{\r\n  \"roomId\" : \"" + roomID + "\",\r\n  \"text\" : \"" + message + "\"\r\n}"
        headers = {
        'Authorization': 'Bearer ' + webexBearerToken,
        'Content-Type': 'application/json'
        }
        #make the API call and save the response into the 'response' variable
        response = requests.request("POST", url, headers=headers, data=payload)
        #evaluate if the response was successful
        # if response.status_code == 200:
            # print("Success!")
        # else:
            # print("Message failed. Code: ", response.status_code)
            # print(response.text)

if __name__ == '__main__':
    changePass()