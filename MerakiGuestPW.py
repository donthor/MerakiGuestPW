import requests
import json
import os
import click
import random
import string

meraki_key = os.environ.get('MERAKI_API_KEY')
baseurl = "https://dashboard.meraki.com/api/v0/networks/"
merakinetwork = os.environ.get('MY_MERAKI_NETWORK')
url = baseurl + str(merakinetwork) + '/ssids/'

@click.command()
@click.option('--pw', type=str, default='', help="Password for SSID - use 'random' to generate 8 character password")
@click.option('--ssid', type=int, default=14, help="SSID number (0-14)")

def changePass(pw, ssid):
    if pw == 'random':
        pw_chars = string.ascii_letters + string.digits
        pw = ''.join(random.choice(pw_chars) for i in range(8))
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

def webexPost():
    pass

if __name__ == '__main__':
    changePass()
    webexPost()