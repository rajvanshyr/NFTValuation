import requests

url = "https://api.twitter.com/2/tweets/search/recent?query=from:worldofwomennft&tweet.fields=public_metrics"

payload={}
headers = {


response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
