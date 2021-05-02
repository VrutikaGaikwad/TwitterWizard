from urllib.request import urlopen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from visualizer import Visualizer
from streamer import Streamer, TwitterClient
from matplotlib.pyplot import show


def pop(text):
    pw = Popup(title="Err..!", content=Label(text=text), size_hint=(None, None), size=(400, 400))
    pw.open()


def net_check():
    try:
        urlopen("https://www.google.com/")
        return True
    except:
        return False


class WindowManager(ScreenManager):
    pass


class Home(Screen):
    pass


class UserBased(Screen):
    username = ObjectProperty(None)
    ntweets = ObjectProperty(None)

    def pie_chart(self):
        if net_check():
            if self.username.text == "":
                pop("Please Enter A User Name!")
            elif self.ntweets.text == "":
                pop("Please Enter Number Of tweets to load!")
            elif not self.ntweets.text.isnumeric():
                pop("Please Enter Numbers Only!")
            else:
                tc = TwitterClient(self.username.text)
                df = tc.get_home_timeline_tweets(int(self.ntweets.text))
                plt = Visualizer.pie_graph(df)
                plt.show()
        else:
            pop("Please check your Internet")

    def line_chart(self):
        if net_check():
            if self.username.text == "":
                pop("Please Enter A User Name!")
            elif self.ntweets.text == "":
                pop("Please Enter Number Of tweets to load!")
            elif not self.ntweets.text.isnumeric():
                pop("Please Enter Numbers Only!")
            else:
                tc = TwitterClient(self.username.text)
                df = tc.get_home_timeline_tweets(int(self.ntweets.text))
                Visualizer.line_graph(df)
                #plt.show()
        else:
            pop("Please check your Internet...")

    def clear(self):
        self.username.text = ""
        self.ntweets.text = ""


class KeywordBased(Screen):

    keyword = ObjectProperty(None)

    def clear(self):
        self.keyword.text = ""

    def get_df(self):
        df = Streamer.stream(self.keyword.text)
        return df

    def pie_chart(self):
        if net_check():
            if self.keyword.text == "":
                pop("Please Enter A Keyword!")
            else:
                plt = Visualizer.pie_graph(self.get_df())
                plt.show()
        else:
            pop("Please check your Internet...")

    def line_chart(self):
        if net_check():
            if self.keyword.text == "":
                pop("Please Enter A Keyword!")
            else:
                Visualizer.line_graph(self.get_df())
                #plt.show()
        else:
            pop("Please check your Internet...")


kv = Builder.load_file("design.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
