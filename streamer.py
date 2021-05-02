import tweepy
import pandas as pd
import twitter_credentials


class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth
    

df = pd.DataFrame(columns=['Tweets', 'User', 'User_statuses_count','User_followers', 'User_location', 'User_verified','fav_count', 'rt_count', 'tweet_date'])
udf = pd.DataFrame(columns=['Tweets', 'User', 'User_statuses_count','User_followers', 'User_location', 'User_verified','fav_count', 'rt_count', 'tweet_date'])

class Streamer():
    
    def __init__(self):
        pass
    
    def stream(data):
        i = 0
        api = tweepy.API(TwitterAuthenticator().authenticate_twitter_app())
        for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='en').items():
            #print(i)
            df.loc[i, 'Tweets'] = tweet.text
            df.loc[i, 'User'] = tweet.user.name
            df.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
            df.loc[i, 'User_followers'] = tweet.user.followers_count
            df.loc[i, 'User_location'] = tweet.user.location
            df.loc[i, 'User_verified'] = tweet.user.verified
            df.loc[i, 'fav_count'] = tweet.favorite_count
            df.loc[i, 'rt_count'] = tweet.retweet_count
            df.loc[i, 'tweet_date'] = tweet.created_at
            i+=1
            if i == 500:
                break
            else:
                pass
        return df

    
class TwitterClient():
    
    def __init__(self, twitter_user):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = tweepy.API(self.auth)

        self.twitter_user = twitter_user

    def get_home_timeline_tweets(self, num_tweets):
        i=0
        #home_timeline_tweets = []
        for tweet in tweepy.Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            #home_timeline_tweets.append(tweet)
            #print(i)
            udf.loc[i, 'Tweets'] = tweet.text
            udf.loc[i, 'User'] = tweet.user.name
            udf.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
            udf.loc[i, 'User_followers'] = tweet.user.followers_count
            udf.loc[i, 'User_location'] = tweet.user.location
            udf.loc[i, 'User_verified'] = tweet.user.verified
            udf.loc[i, 'fav_count'] = tweet.favorite_count
            udf.loc[i, 'rt_count'] = tweet.retweet_count
            udf.loc[i, 'tweet_date'] = tweet.created_at
            i+=1
            if i == num_tweets:
                break
            else:
                pass
        #print(udf)
        #print(home_timeline_tweets)
        return udf


##df=Streamer.stream('modi')
##print(df['fav_count'].values)

#tc=TwitterClient('Cevans')
#tc.get_home_timeline_tweets(5)

