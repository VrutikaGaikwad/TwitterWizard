import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import numpy as np
from analyzer import Analyzer as ay


def percentage(part, whole):
    temp = 100 * float(part) / float(whole)
    return format(temp, '.2f')


class Visualizer():

    def __init__(self):
        pass

    def pie_graph(df):
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0
        sentiment_array = np.array([ay.tweet_analyzer(ay.clean_tweet(tweet)) for tweet in df['Tweets']])
        # print(sentiment_array)

        for i in range(len(sentiment_array)):
            if sentiment_array[i] == "neutral":
                neutral += 1
            elif sentiment_array[i] == "wpositive":
                wpositive += 1
            elif sentiment_array[i] == "positive":
                positive += 1
            elif sentiment_array[i] == "spositive":
                spositive += 1
            elif sentiment_array[i] == "wnegative":
                wnegative += 1
            elif sentiment_array[i] == "negative":
                negative += 1
            elif sentiment_array[i] == "snegative":
                snegative += 1

        positive = percentage(positive, len(sentiment_array))
        wpositive = percentage(wpositive, len(sentiment_array))
        spositive = percentage(spositive, len(sentiment_array))
        negative = percentage(negative, len(sentiment_array))
        wnegative = percentage(wnegative, len(sentiment_array))
        snegative = percentage(snegative, len(sentiment_array))
        neutral = percentage(neutral, len(sentiment_array))

        labels = ['Positive ' + str(positive) + '%', 'Weakly Positive ' + str(wpositive) + '%',
                  'Strongly Positive ' + str(spositive) + '%', 'Neutral ' + str(neutral) + '%',
                  'Negative ' + str(negative) + '%', 'Weakly Negative ' + str(wnegative) + '%',
                  'Strongly Negative ' + str(snegative) + '%']
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        #plt.show()
        return plt

    def line_graph(df):
        style.use("ggplot")
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        sentiment_array = np.array([ay.tweet_analyzer(ay.clean_tweet(tweet)) for tweet in df['Tweets']])

        def animate(i):
            xar = []
            yar = []
            zar = []
            x = 0
            y = 0
            z = 0

            for sentiment in sentiment_array:
                x += 1
                if sentiment == "positive" or sentiment == "wpositive" or sentiment == "spositive":
                    y += 1
                elif sentiment == "negative" or sentiment == "wnegative" or sentiment == "snegative":
                    z += 1
                else:
                    pass

                xar.append(x)
                yar.append(y)
                zar.append(z)

            ax1.clear()
            ax1.plot(xar, yar,zar)

        ani = animation.FuncAnimation(fig, animate, interval=1000, save_count=1000)
        plt.show()
