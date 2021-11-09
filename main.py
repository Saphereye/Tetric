from interpreter import converter
import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

inputText = ''


class MyGrid(Widget):
    global inputText
    inputText = ObjectProperty(None)

    def convert(self):
        self.inputText = converter(inputText)


class TETRICApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    TETRICApp().run()

"""
		GridLayout:
			cols:1
			Button:
				text:"Reset"
				on_press:root.reset()
		GridLayout:
			cols:1
			Button:
				text:"Exit"
				background_color: (1,0,0, 1.0)
				on_press:app.stop()
"""
