import requests
import json
import os
import click
import random
import string

meraki_key = os.environ.get('MERAKI_API_KEY')
webexBearerToken = "os.environ.get('WEBEX_BEARER_TOKEN')"
baseurl = "https://dashboard.meraki.com/api/v0/networks/"
merakinetwork = os.environ.get('MY_MERAKI_NETWORK')

@click.command()
@click.option('--pw', type=str, default='', help="Password for SSID - use 'random' to generate 8 character password")
@click.option('--ssid', type=int, default=14, help="SSID number (0-14)")
def changePass(pw, ssid):
    if pw == 'random':
        pw_chars = string.ascii_letters + string.digits
        pw = ''.join(random.choice(pw_chars) for i in range(8))
    url = baseurl + str(merakinetwork) + '/ssids/'
    payload = json.dumps(
    {"enabled": False,
    "psk": pw
    })
    headers = {
    'X-Cisco-Meraki-API-Key': meraki_key,
    'Content-Type': 'application/json'
    }
    response_get = requests.get(url + str(ssid), headers=headers)
    data = response_get.json()
    print(f'Please confirm change to SSID: {data["name"]} with password: {pw}')
    while (answer:=input("Do you want to continue? (Enter y/n)").lower() ) not in {"y", "n"}: pass
    if answer == 'y':
        response = requests.request("PUT", url + str(ssid), headers=headers, data=payload)
        print(response.status_code)
        if response.status_code == 200:
            click.echo('Password Modified')
        print(response.text)

    #Post in Webex
    #read input from the user and set it to the 'message' variable
    message = f'The new password is {pw}'
    #set the 'url' variable to the webex url
    url = "https://api.ciscospark.com/v1/messages"
    roomID = "Y2lzY29zcGFyazovL3VzL1JPT00vMmJiYzBjOTAtYWRjYy0xMWViLWEyYmItMzE1ZDJkMTgxMmJj"
    #define body and header data
    payload="{\r\n  \"roomId\" : \"" + roomID + "\",\r\n  \"text\" : \"" + message + "\"\r\n}"
    headers = {
    'Authorization': 'Bearer NTI1YWNjYmYtZmQyZS00MTlkLWIzNTAtNzY2NWQxMDRkYzA4MzZkMWVkYTgtYTlm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f',
    'Content-Type': 'application/json'
    }

    #make the API call and save the response into the 'response' variable
    response = requests.request("POST", url, headers=headers, data=payload)
    #evaluate if the response was successful
    if response.status_code == 200:
        print("Success!")
    else:
        print("Message failed. Code: ", response.status_code)
        print(response.text)

if __name__ == '__main__':
    changePass()