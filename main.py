from kivy.app import App
from kivy.uix.button import Button

class HelloApp(App):
    def build(self):
        return Button(text="¡Hola Mundo!")

if __name__ == '__main__':
    HelloApp().run()
