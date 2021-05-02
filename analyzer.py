import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


class Analyzer():

    def __init__(self):
        pass

    def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def tweet_analyzer(tweet):
        analysis = TextBlob(tweet)
        # print(analysis.sentiment)  # print tweet's polarity
        # polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

        if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
            return "neutral"
        elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
            return "wpositive"
        elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
            return "positive"
        elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
            return "spositive"

        elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
            return "wnegative"
        elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
            return "negative"
        elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
            return "snegative"
