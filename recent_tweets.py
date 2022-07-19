import requests

url = "https://api.twitter.com/2/tweets/search/recent?query=from:worldofwomennft&tweet.fields=public_metrics"

payload={}
headers = {
  'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIIPZwEAAAAAk7fYGykK2OfFD6UqGLdM69%2FbsK4%3DZ0XCZHTzkKEzNxJRNVmJ2PZE6TRGFHlZtBAp8LEuXeQdGkJ66h',
  'Cookie': 'guest_id=v1%3A164823485883999963; guest_id_ads=v1%3A164823485883999963; guest_id_marketing=v1%3A164823485883999963; personalization_id="v1_RHU8DjqAQNnxprY6Sd740g=="'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)