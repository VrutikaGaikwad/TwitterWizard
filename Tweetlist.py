from kivy.app import App
from kivy.lang import Builder
from streamer import Streamer, TwitterClient
from kivy.uix.recycleview import RecycleView


Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        sfile = open("screendata.txt", "r+")
        fword = sfile.readline()
        nword = sfile.readline()
        if nword != '':
            df = Streamer.stream(sfile)
            self.data = [{'text': x} for x in df['Tweets']]
        else:
            tc = TwitterClient(fword)
            df = tc.get_home_timeline_tweets(int(nword))
            self.data = [{'text': x} for x in df['Tweets']]


class TestApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()
