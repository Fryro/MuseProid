from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
#from database import DataBase

class MainScreenWindow(Screen):
    current_song = ObjectProperty(None)
    next_song = ObjectProperty(None)
    previous_song = ObjectProperty(None)
    song_state = False
    time_stamp_song = ObjectProperty(None)

    current_song = "song 5"
    next_song = "song 6"
    previous_song = "song 4"
    song_state = False
    time_stamp_song = "1.24"

    def PausePlaySong(self):
        song_state = False
        if (song_state == False):
            print("Song State : False")
        elif (song_state == True):
            print("Song State : True")
        else:
            print("NO STATE")
            return
        print("Song State : {}".format(song_state))

    def LastSong(self):
        print("Last Song Pressed")
        self.update(-1)

    def NextSong(self):
        print("Next Song Pressed")
        self.update(1)

    def LibraryButton(self):
        print("Going to Library...")
        sm.current = "library"

    def update(self, direction):
        print("Button Pressed")
        #current_song += direction
        #next_song += direction
        #previous_song += direction
        #time_stamp_song = 0
        #print("Last Song : {}\nNext Song : {}\n\tThis Song : {}\t\tSong Time : {}".format(previous_song, next_song, current_song, time_stamp_song))
        print("PRESSED")
        sm.current = "main"

class SongSelectionMenu(Screen):
    song = ObjectProperty(None)
    listS = ObjectProperty(None)

    def PlayButton(self):
        print("Playing THIS song.")
    
    def BackButton(self):
        sm.current = "main"    

    def InfoButton(self):
        sm.current = "info"

class ProidMainWindow(Screen):
    n = ObjectProperty(None)
    current_s = ObjectProperty(None)
    last_s = ObjectProperty(None)
    next_s = ObjectProperty(None)
    time_stamp_s = ObjectProperty(None)
    
    def BackButton(self):
        print("Going Back...")
        sm.current = "library"

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

sm = WindowManager()
#db = DataBase("users.txt")

screens = [MainScreenWindow(name="main"), SongSelectionMenu(name="library"), ProidMainWindow(name="info")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()
