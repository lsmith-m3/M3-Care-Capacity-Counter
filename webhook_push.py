import json
import urllib.request
import time

# Load configuration from JSON file
with open('config.json', 'r') as file:
    config = json.load(file)

counterMac = config['counterMac']
counterToken = config['counterToken']
numberToShow = config['numberToShow']
increase_amount = config['increase_amount']
delay_minutes = config['delay_minutes']

def push_number_to_smiirl(number):
    url = f"http://api.smiirl.com/{counterMac}/set-number/{counterToken}/{number}"
    try:
        req = urllib.request.Request(url)
        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))
        
        if 'status' in cont and cont['status'] == 200:
            print(f"Number {number} successfully pushed to Smiirl counter.")
            return True
        else:
            print(f"Failed to push number {number}. Status: {cont['status']}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Loop to update numberToShow every 5 minutes
while True:
    success = push_number_to_smiirl(numberToShow)
    if success:
        numberToShow += increase_amount
        print(f"Next number will be {numberToShow}")
    time.sleep(delay_minutes * 60)
