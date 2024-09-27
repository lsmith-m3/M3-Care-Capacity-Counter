import urllib, json
import urllib.request
import time  # For adding delay

# Change those lines to fit your device (check it on https://my.smiirl.com) and your data
counterMac = 'e08e3c37e386'
counterToken = 'cb8822a2b6ef2b1391aa1ba55c08c5b5'
numberToShow = 204960  # Initial number to show
increase_amount = 10  # Amount to increase by each time
delay_minutes = 5     # Time delay in minutes

def push_number_to_smiirl(number):
    url = f"http://api.smiirl.com/{counterMac}/set-number/{counterToken}/{number}"
    try:
        req = urllib.request.Request(url)
        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))
        
        # Check if the API response status is 200
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
    # Push the current number to the Smiirl counter
    success = push_number_to_smiirl(numberToShow)

    if success:
        # Increase numberToShow by 10
        numberToShow += increase_amount
        print(f"Next number will be {numberToShow}")

    # Wait for 5 minutes before sending the next request
    time.sleep(delay_minutes * 60)
