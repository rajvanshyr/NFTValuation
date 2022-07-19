import requests
from datetime import datetime
from datetime import timedelta
import pandas as pd 


users={'rudekidznft','BoredApeYC','VeeFriends','doodles','worldofwomennft','AzukiOfficial'}
df=pd.DataFrame()

for a in users:
	url = "https://api.twitter.com/2/users/by/username/"
	url=url+a
	final=url+"?user.fields=public_metrics"

	recent="https://api.twitter.com/2/tweets/search/recent?query=from:"
	recent=recent+a+"&tweet.fields=public_metrics,created_at"

	payload={}
	headers = {
	  'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIIPZwEAAAAAk7fYGykK2OfFD6UqGLdM69%2FbsK4%3DZ0XCZHTzkKEzNxJRNVmJ2PZE6TRGFHlZtBAp8LEuXeQdGkJ66h',
	  'Cookie': 'guest_id=v1%3A164823485883999963; guest_id_ads=v1%3A164823485883999963; guest_id_marketing=v1%3A164823485883999963; personalization_id="v1_RHU8DjqAQNnxprY6Sd740g=="'
	}

	response = requests.request("GET", final, headers=headers, data=payload)
	print("curr "+a)
	followers=response.json()['data']['public_metrics']['followers_count']
	response2 = requests.request("GET", recent, headers=headers, data=payload)
	print("timestamp 1 "+ str(response2.json()))
	timestamp1= response2.json()['data']
	#[0]['created_at']
	#csv of text, likes rts and time diffetnce to get engamnet per hour then compare to overall followers and market cap
	d={}
	for x in timestamp1:
		d={}
		pm=x['public_metrics']
		d['user']=a
		d['tweet']=x['text']
		d['retweet_count']=pm['retweet_count']
		d['reply_count']=pm['reply_count']
		d['like_count']=pm['like_count']
		d['quote_count']=pm['quote_count']
		d['followers']=followers
		ts=x['created_at']
		t1 = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fZ")
		now = (datetime.now()+timedelta(hours=7))
		d['difference']=str(now-t1)
		d['seconds']=str((now-t1).total_seconds())
		#print("now "+str(now) )
		#print("t1 "+ str(t1))
		#print(response2.json()['data'][0]['text'])
		#print("difference"+str(now-t1))
		df=df.append(d,ignore_index=True)
		print(df.tail())


df.to_csv('eng.csv')