from datetime import datetime
import time
import requests

current_time = datetime.now()
starttime = time.time()

print("Twitch Username:")

while True:
	channelName = str(input())
	
	contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')
	
	special_characters = "\"!@#$%^&*()-+?_=,<>/\""
	
	if ' ' in channelName:
		print("That channel does not exist!")
	
	else:
		
		if any (c in special_characters for c in channelName):
			print("That channel does not exist!")
		
		else:
			
			if 'isLiveBroadcast' in contents:
				print("------------------------------------------------")
				print(channelName + ' is currently streaming!')
			else:
				print("------------------------------------------------")
				print(channelName + ' is not currently streaming!')
	
	print (datetime.today().strftime('%H:%M:%S'  " GMT"), datetime.today().strftime('      %d-%m-%Y'))
	print("------------------------------------------------")
	time.sleep(15.0 - ((time.time() - starttime) % 15.0))