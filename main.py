import sys
import traceback
import os
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import mainthread
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import serial_geotab as gt

# ==================== MANEJADOR DE ERRORES GLOBAL ====================
def global_exception_handler(exc_type, exc_value, exc_traceback):
    """Captura cualquier excepción no manejada y la guarda en un archivo"""
    try:
        # Intentar guardar en Documentos (Android) o carpeta actual
        possible_paths = [
            '/storage/emulated/0/Documents/error_log.txt',
            '/storage/emulated/0/Download/error_log.txt',
            '/sdcard/Documents/error_log.txt',
            '/sdcard/Download/error_log.txt',
            'error_log.txt',  # carpeta local
        ]
        log_path = None
        for path in possible_paths:
            try:
                dir_path = os.path.dirname(path)
                if dir_path and not os.path.exists(dir_path):
                    continue
                log_path = path
                break
            except:
                continue
        
        if log_path is None:
            log_path = 'error_log.txt'
        
        with open(log_path, 'a') as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"ERROR CAPTURADO: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*60}\n")
            traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)
            f.write(f"\n")
        
        print(f"Error guardado en: {log_path}")
        
    except Exception as e:
        print(f"Error crítico al guardar log: {e}")
        traceback.print_exception(exc_type, exc_value, exc_traceback)

# Instalar el manejador global de excepciones
sys.excepthook = global_exception_handler

# ==================== CÓDIGO PRINCIPAL ====================

class GeotabApp(App):
    def build(self):
        try:
            # Cargar la interfaz desde el archivo KV
            return Builder.load_file('geotab_gui.kv')
        except Exception as e:
            global_exception_handler(type(e), e, e.__traceback__)
            from kivy.uix.label import Label
            return Label(text=f"Error cargando UI: {e}")
    
    def on_start(self):
        try:
            # Mostrar popup de información al inicio
            self.show_info_popup()
            
            # Conectar a Geotab
            self.api = gt.authenticate_geotab()
            self.update_status("Geotab conectado")
        except Exception as e:
            global_exception_handler(type(e), e, e.__traceback__)
            self.api = None
            self.update_status(f"Error Geotab: {str(e)[:50]}")
    
    def show_info_popup(self):
        content = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        titulo = Label(
            text="[b]CONTROL DE ILUMINACIÓN[/b]",
            markup=True,
            font_size='18sp',
            size_hint_y=0.2
        )
        
        desarrollador = Label(
            text="[b]Desarrollado por:[/b]\nLuis Manríquez\nJosé André Paredes",
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
            global_exception_handler(type(e), e, e.__traceback__)
            self.update_status(f"Error: {str(e)[:30]}")
    
    @mainthread
    def update_status(self, msg):
        try:
            self.root.ids.status.text = f"Status: {msg}"
        except:
            pass

if __name__ == "__main__":
    GeotabApp().run()
