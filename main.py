import requests


channelName = 'loltyler1'

contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')

if 'isLiveBroadcast' in contents: 
    print(channelName + ' is live')
else:
    print(channelName + ' is not live')