import requests

url = "https://testnets-api.opensea.io/api/v1/assets?order_by=sale_count&order_direction=desc&offset=0&limit=20&include_orders=false"

response = requests.get(url)

r= response.json()['assets']
l=[]
for x in r:
	d={}
	d['name']=x['name']
	d['token_id']=x['token_id']
	d['num_sales']=x['num_sales']
	d['collection']=x['collection']['slug']
	l.append(d)


print(l) 

urlc = "https://testnets-api.opensea.io/api/v1/collection/"

for y in l:
	print(y['collection'])
	urln=urlc+y['collection']+"/stats"
	response = requests.get(urln)
	print(response.text)



#Retrive top 20 NFTs using orderby param sale_count

#get various statistic on them 

#Input: number of sales(can scrape from opensea), social following(can scrape on twitter )



