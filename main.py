import requests


channelName = 'STREAMERNAME'

if ' ' in channelName:
  print("Input invalid.")
else:

  contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')

  if 'isLiveBroadcast' in contents: 
    print(channelName + ' is live')
  else:
    print(channelName + ' is not live')