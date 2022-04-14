print("NUMBER ONE... WORKING...")
import requests

channelName = 'STREAMERNAME'
print("NUMBER TWO... WORKING...")

contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')

special_characters = "\"!@#$%^&*()-+?_=,<>/\""

if ' ' in channelName:
	print("That channel does not exist!")

else:
	
	if any (c in special_characters for c in channelName):
		print("That channel does not exist!")
	
	else:
		if 'isLiveBroadcast' in contents:
			print(channelName + ' is live')
		else:
			print(channelName + ' is not live')