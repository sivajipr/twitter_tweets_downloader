import oauth2 as oauth
import json

Consumer_Key = "************************************"
Consumer_Secret = "*********************************"
Access_Key = "**************************************"
Access_Secret = "***********************************"

consumer = oauth.Consumer(key=Consumer_Key, secret=Consumer_Secret)
access_token = oauth.Token(key=Access_Key, secret=Access_Secret)
client = oauth.Client(consumer, access_token)

name =raw_input("Enter the twitter username: ")


post = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count=10"

response, data = client.request(post)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']
