from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class PopupApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Función para mostrar el mensaje "Hola" en la ventana emergente
        def show_popup(instance):
            popup = Popup(title='Mensaje',
                          content=Button(text='Hola'),
                          size_hint=(None, None), size=(200, 200))
            popup.open()
        
        # Crear un botón
        button = Button(text='Mostrar mensaje')
        # Asignar la función show_popup al evento on_press del botón
        button.bind(on_press=show_popup)
        
        # Agregar el botón al diseño
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    PopupApp().run()
