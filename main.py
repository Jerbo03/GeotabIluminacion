from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import mainthread
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import serial_geotab as gt

class GeotabApp(App):
    def build(self):
        # Cargar la interfaz desde el archivo KVmaxi
        return Builder.load_file('geotab_gui.kv')
    
    def on_start(self):
        # Mostrar popup de información al inicio
        self.show_info_popup()
        
        # Conectar a Geotab
        try:
            self.api = gt.authenticate_geotab()
            self.update_status("Geotab conectado")
        except Exception as e:
            self.api = None
            self.update_status(f"Error Geotab: {e}")
    
    def show_info_popup(self):
        # Crear contenido del popup
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        titulo = Label(
            text= "[b]CONTROL DE ILUMINACIÓN[/b]",
            markup=True,
            font_size='18sp',
            size_hint_y=0.2
        )
        
        desarrollador = Label(
            text="[b]Desarrollado por:[/b]\nLuis Manrique\nJosé André Paredes",
            markup=True,
            size_hint_y=0.3
        )
        
        contacto = Label(
            text="[b]Contacto:[/b]\nlmanriqu@fmi.com\njparedes5@fmi.com",
            markup=True,
            size_hint_y=0.3
        )
        
        version = Label(
            text="[b]Versión:[/b] 1.0.0\n[b]Fecha:[/b] 2026",
            markup=True,
            size_hint_y=0.2
        )
        
        cerrar_btn = Button(
            text="Aceptar y Continuar",
            size_hint_y=0.1,
            background_color=(0.2, 0.6, 0.2, 1)
        )
        
        content.add_widget(titulo)
        content.add_widget(desarrollador)
        content.add_widget(contacto)
        content.add_widget(version)
        content.add_widget(cerrar_btn)
        
        popup = Popup(
            title='Información de la Aplicación',
            content=content,
            size_hint=(0.85, 0.7),
            auto_dismiss=False
        )
        
        cerrar_btn.bind(on_release=lambda x: popup.dismiss())
        popup.open()
    
    def send_action(self, accion):
        if not self.api:
            self.update_status("Geotab no conectado")
            return
        try:
            gt.apagar_prender_luces(self.api, accion)
            self.update_status(f"Comando enviado: {accion.upper()}")
        except Exception as e:
            self.update_status(f"Error: {e}")
    
    @mainthread
    def update_status(self, msg):
        self.root.ids.status.text = f"Status: {msg}"

if __name__ == "__main__":
    GeotabApp().run()
