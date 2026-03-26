from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.button import Button

class AntivirusShield(App):
    def build(self):
        self.title = "Antivirus Shield Pro"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(text="🛡️ SECURITY DASHBOARD", font_size='28sp', bold=True))
        
        features = [("Hide Live Location", True), ("Block Unknown Calls", False), ("Auto-Clean Malware", True)]
        for text, active in features:
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            row.add_widget(Label(text=text, halign='left'))
            row.add_widget(Switch(active=active))
            layout.add_widget(row)

        layout.add_widget(Label(text="Status: [color=00ff00]SYSTEM PROTECTED[/color]", markup=True))
        layout.add_widget(Button(text="RUN DEEP SCAN", size_hint_y=None, height=60))
        return layout

if __name__ == "__main__":
    AntivirusShield().run()

