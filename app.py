import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

WEBEX_KEY = os.environ['WEBEX_API_KEY']
WEBEX_USER = os.environ['WEBEX_USER']

def main():
    light = checkforlight()
    if not light:
        exit()
    else:
        status = getWebexStatus()
        if status == 'active':
            setLightGreen()
        elif status == 'presenting':
            setLightPurple()
        elif status == 'meeting':
            setLightYellow()
        elif status == 'call':
            setLightYellow()
        elif status == 'inactive':
            setLightBlue()
        elif status == 'DoNotDisturb':
            setLightRed()
        return


def getWebexStatus():

    url = "https://webexapis.com/v1/people/" + WEBEX_USER

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + WEBEX_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print (json.loads(response.text)['status'])
    return json.loads(response.text)['status']


def checkforlight():
    url = 'http://localhost:8989?action= currentpresence'
    response = requests.request("GET", url)
    if 'NO_DEVICE' in response.text:
        return False
    else:
        return True


def setLightGreen():
    url = "http://localhost:8989?action=light&red=0&green=100&blue=0"
    setcolour = requests.request("GET",url)
    return setcolour


def setLightYellow():
    url = "http://localhost:8989?action=light&red=100&green=100&blue=0"
    setcolour = requests.request("GET",url)
    return setcolour


def setLightOrange():
    url = "http://localhost:8989?action=light&red=200&green=50&blue=0"
    setcolour = requests.request("GET",url)
    return setcolour


def setLightRed():
    url = "http://localhost:8989?action=light&red=100&green=0&blue=0"
    setcolour = requests.request("GET",url)
    return setcolour


def setLightPurple():
    url = "http://localhost:8989?action=light&red=100&green=0&blue=100"
    setcolour = requests.request("GET",url)
    return setcolour


def setLightBlue():
    url = "http://localhost:8989?action=light&red=0&green=0&blue=100"
    setcolour = requests.request("GET",url)
    return setcolour


if __name__ == "__main__":
    main()