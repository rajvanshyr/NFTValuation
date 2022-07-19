import requests
from datetime import timedelta
import pandas as pd 

  
# explicit function  
#input lis of NFT names 
#output Df with NFt important metrics    
def lookup_tweets(NFT_names):
	print("GFG")
	df=pd.DataFrame()
	for x in NFT_names:
		url = "https://api.twitter.com/2/tweets/search/recent?query="+x
		url=url+"&start_time=2022-07-08T10:00:00-05:00&max_results=35&tweet.fields=public_metrics"

		payload={}
		headers = {
		  'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIIPZwEAAAAAk7fYGykK2OfFD6UqGLdM69%2FbsK4%3DZ0XCZHTzkKEzNxJRNVmJ2PZE6TRGFHlZtBAp8LEuXeQdGkJ66h',
		  'Cookie': 'guest_id=v1%3A164823485883999963; guest_id_ads=v1%3A164823485883999963; guest_id_marketing=v1%3A164823485883999963; personalization_id="v1_RHU8DjqAQNnxprY6Sd740g=="'
		}

		response = requests.request("GET", url, headers=headers, data=payload)
		data=response.json()['data']
		for x in data:

			rts=x['public_metrics']['retweet_count']
			likes=x['public_metrics']['like_count']

		print(response.text)
