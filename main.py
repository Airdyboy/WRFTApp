import kivy
#kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.factory import Factory
from kivy.utils import boundary
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.audio import SoundLoader

from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

sm = ScreenManager()
catchRecord_screen = Screen(name='catchRecord')
sm.add_widget(catchRecord_screen)

class home_screen(Screen):
    '''
    This is where the setting up for buttons for the home screen goes
    '''
    pass

class catchRecord_screen(Screen):
    '''
    This is where the setting up for buttons for the home screen goes
    '''
    pass


sm.add_widget(home_screen(name='home'))
sm.add_widget(catchRecord_screen(name='home'))

class WRFT(App):
    def build(self):
        return Button(text='Record your catch')
    
    def recordCatch_process(self, catchList):
        """
        Clear screen
        Go to screen with Collection points for Weight, photo, name of fish etc [Populate screen]
        Input the output of them to a Dictionary
        """
        
    def out2Database(self, catchList, serverNo):
        '''
        Change data from databases to outputtable form
        Send data to database
        '''
    
    def weatherForcast_Detect(self, touch):
        -pass
    
    
class WeatherForecast(App):
    def build(self):
        return Button(text='Weather Forecast')

class FishingLocations(App):
    def build(self):
        return Button(text='Local Fishing Locations')

sm.add_widget(home_screen(name='home'))
sm.add_widget(catchRecord_screen(name='home'))

if __name__ == '__main__':
    WRFT().run()






