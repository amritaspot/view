import sys
import os
import numpy as np
#import cv2
import PIL
#from picamera import PiCamera
#import RPi.GPIO as GPIO
import matplotlib
import time
from time import sleep
import scipy
from scipy.signal import find_peaks, peak_widths, peak_prominences
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.lang import Builder
from random import random
import matplotlib.pyplot as plt
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.dropdown import DropDown
from datetime import date, datetime
from subprocess import call
from kivy.properties import ListProperty

#==============================================================================
#camera = PiCamera()
def shutdown():
    pass

def call_support():
    pass

def training_mode():
    pass

def network_setup(self, *kwargs):
        self.manager.current = 'setup_network'
    pass

class release(Screen):
    def __init__(self, **kwargs):
        super(release, self).__init__(**kwargs)
        Clock.schedule_once(self.change_screen, 5)

    def change_screen(self, *kwargs):
        self.manager.current = 'setup_splash'
    pass

class setup_splash(Screen):
    pass

class setup_network(Screen):
    pass

class setup_LIS(Screen):
    pass

class mainsplash(Screen):
    pass

class homepage(Screen):
    pass

class main_testtype(Screen):
    pass

class main_caltype(Screen):
    pass

class main_reqid(Screen):
    pass

class main_calid(Screen):
    pass

class main_analyte(Screen):
    pass

class main_instruction(Screen):
    pass

class main_cardtestresult(Screen):
    pass

class main_urinestripresult(Screen):
    pass

class main_colorimeterresult(Screen):
    pass

class main_nephelometerresult(Screen):
    pass

class main_resultdata(Screen):
    pass

class errorcodes(Screen):
    pass

kv = Builder.load_file("release.kv")
sm = ScreenManager()
sm.add_widget(release(name='release'))
sm.add_widget(setup_splash(name='setup_splash'))
sm.add_widget(setup_network(name='setup_network'))
sm.add_widget(setup_LIS(name='setup_LIS'))
sm.add_widget(mainsplash(name='mainsplash'))
sm.add_widget(homepage(name='homepage'))
sm.add_widget(main_testtype(name='main_testtype'))
sm.add_widget(main_caltype(name='main_caltype'))
sm.add_widget(main_reqid(name='main_reqid'))
sm.add_widget(main_calid(name='main_calid'))
sm.add_widget(main_analyte(name='main_analyte'))
sm.add_widget(main_instruction(name='main_instruction'))
sm.add_widget(main_cardtestresult(name='main_cardtestresult'))
sm.add_widget(errorcodes(name='errorcodes'))
sm.add_widget(main_urinestripresult(name='main_urinestripresult'))
sm.add_widget(main_colorimeterresult(name='main_colorimeterresult'))
sm.add_widget(main_nephelometerresult(name='main_nephelometerresult'))
sm.add_widget(main_resultdata(name='main_resultdata'))

class MainApp(App):
    def build(self):
        Window.size = (800, 500)
        return sm

if __name__=="__main__":
    sa = MainApp()
    sa.run()
