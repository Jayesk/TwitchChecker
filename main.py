from datetime import datetime
import time
import requests
	
current_time = datetime.now()
starttime = time.time()

twitchuser = input("Twitch Username: ")
if len(twitchuser) > 20:
	print("Checking " + twitchuser + "...")
	print("------------------------------------------------")
	print("That channel name is too long!")
	print (datetime.today().strftime('%H:%M:%S'  " GMT"), datetime.today().strftime('     %d-%m-%Y'))
	print("------------------------------------------------")

else:

	print("Checking " + twitchuser + "...")

	channelName = twitchuser
	
	contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')
		
	special_characters = "\"!@#:;`'~*$£¬%^&*()-+?_=,<>/\.,\""
	
	
	
	if ' ' in channelName:
		print("------------------------------------------------")
		print("Channel names cannot have spaces!")
		print (datetime.today().strftime('%H:%M:%S'  " GMT"), datetime.today().strftime('     %d-%m-%Y'))
		print("------------------------------------------------")
		
	else:
			
		if any (c in special_characters for c in channelName):
			print("------------------------------------------------")
			print("Channel names cannot have special characters!")
			print (datetime.today().strftime('%H:%M:%S'  " GMT"), datetime.today().strftime('     %d-%m-%Y'))
			print("------------------------------------------------")
			
		else:
	
			while True:
				
				if 'isLiveBroadcast' in contents:
					print("------------------------------------------------")
					print(channelName + ' is currently streaming!')
					print (datetime.today().strftime('%H:%M:%S'  " GMT"), datetime.today().strftime('     %d-%m-%Y'))
					print("------------------------------------------------")
					
				else:
					print("------------------------------------------------")
					print(channelName + ' is not currently streaming!')
					print (datetime.today().strftime('%H:%M:%S'  " GMT"), datetime.today().strftime('     %d-%m-%Y'))
					print("------------------------------------------------")
		
				time.sleep(15.0 - ((time.time() - starttime) % 15.0))