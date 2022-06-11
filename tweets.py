# some useful module
import snscrape.modules.twitter as sntwitter
import pandas as pd

query="(from:elonmusk) until:2022-06-10 since:2020-01-01"

limit=0
data=[]

# function to gather twitter data 
def data_frame(limit=0):
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        dataframe={}
        limit=limit+1

        dataframe['Serial No']=limit
        dataframe['User']=str(tweet.user)[20:]
        dataframe['User Account']=str(tweet.user)
        dataframe['Content']=tweet.content
        dataframe['Url']=tweet.url
        dataframe['Date']=str(tweet.date)[:10]
        dataframe['Time']=str(tweet.date)[11:19]
        dataframe['Time Zone']=str(tweet.date)[19:]

        if (limit)>500:
            break
        data.append(dataframe)

# function to save tweets in excel file 
def save_excel(data,file_name="tweets.xlsx",Index=False):
    df=pd.DataFrame(data)
    df.to_excel(file_name,index=Index)
    print("done!!")


data_frame()

save_excel(data,"tweets.xlsx")

