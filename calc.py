import pandas as pd 

df=pd.read_csv('eng.csv')
df2=pd.DataFrame()
#print(df.head())

curr=df.iloc[0]['user']
cum_score=0
time=0
avgd={}

for index, row in df.iterrows():
	if row['user'] != curr:
		hrs=time/(60*60)
		avg=cum_score/hrs
		avgd[curr]=avg
		cum_score=0
		time=0
		curr=row['user']

	d=row.to_dict()
	score=((row['retweet_count']*3)+(row['reply_count']*3)+(row['quote_count']*2)+row['like_count'])
	d['score']=score
	cum_score+=score
	time+=row['seconds']
	df2=df2.append(d,ignore_index=True)


hrs=time/(60*60)
avg=cum_score/hrs
avgd[curr]=avg
df3=pd.DataFrame()
#print("rude avg"+str(avg))
for index, row in df2.iterrows():
	d=row.to_dict()
	d['avg_score']=avgd[d['user']]
	df3=df3.append(d,ignore_index=True)


df3.to_csv('score.csv')
print(avgd)



#next steps build ai, backtest
