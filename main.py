from kivy.uix.screenmanager import ScreenManager, Screen
import datetime
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from datetime import datetime
from kivy.lang import Builder


from kivy.clock import Clock
from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog


class HistoryWindow(Screen):

    Builder.load_file('historywindow.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.data_)

    def data_(self, *args):

        # Add more texts as needed
        generated_texts = ['Text1', 'Text2', 'Text3',
                           'Text3', 'Text3', 'Text3', 'Text3']

        for generated_text in generated_texts:
            self.identity = '2 Detected'
            self.background_color = (321/255, 245/255, 245/255, 1)
            self.icon = 'check'
            self.color = [0, 0, 0, 1]
            self.identity_color = [224/255, 224/255, 224/255, 1]
            self.identity_bg = [1, 1, 1, 1]
            self.id_text_color = [1, 1, 1, 1]
            self.date = 'Wednesday, November 8, 2023'

            add_bot = Chats(
                text=generated_text, identity=self.identity, background_color=self.background_color, icon=self.icon, context_color=self.color, identity_color=self.identity_color, identity_bg=self.identity_bg, id_text_color=self.id_text_color, date=self.date)

            self.ids.listexpenses.add_widget(add_bot)

    def view_history(self):
        self.manager.current = "detailedhistory"
        self.manager.transition.direction = "left"


class DetailedHistoryWindow(Screen):

    Builder.load_file('detailedhistory.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.data_)

    def data_(self, *args):

        # Add more texts as needed
        generated_texts = ['Text1', 'Text2', 'Text3',
                           'Text3', 'Text3', 'Text3', 'Text3']

        for generated_text in generated_texts:
            self.identity = '2 Detected'
            self.background_color = (321/255, 245/255, 245/255, 1)
            self.icon = 'check'
            self.color = [0, 0, 0, 1]
            self.identity_color = [224/255, 224/255, 224/255, 1]
            self.identity_bg = [1, 1, 1, 1]
            self.id_text_color = [1, 1, 1, 1]
            self.date = 'Wednesday, November 8, 2023'

            add_bot = Chats(
                text=generated_text, identity=self.identity, background_color=self.background_color, icon=self.icon, context_color=self.color, identity_color=self.identity_color, identity_bg=self.identity_bg, id_text_color=self.id_text_color, date=self.date)

            self.ids.detailed_history.add_widget(add_bot)

    def switch_to_main(self):
        self.manager.current = "history"
        self.manager.transition.direction = "right"


class CustomLabel(MDLabel):
    pass


class DialogContent(MDBoxLayout):

    """Customize dialog box for user to insert their expenses"""
    # Initiliaze date to the current date

    def cancel(self):
        MDApp.get_running_app().root.settings.close_dialog()


class Chats(MDCard):
    text = StringProperty()
    identity = StringProperty()
    date = StringProperty()
    background_color = ColorProperty()
    icon = StringProperty()
    context_color = ColorProperty()
    identity_color = ColorProperty()
    identity_bg = ColorProperty()
    id_text_color = ColorProperty()

    def switch_screen(self):
        self.task_list_dialog = MDDialog(
            title="Detected Berry",
            type="custom",
            size_hint_x=0.9,
            size_hint_y=None,
            content_cls=DialogContent(),
        )

        self.task_list_dialog.open()

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()


class WindowManager(ScreenManager):
    pass


class rawApp(MDApp):

    def build(self):

        return WindowManager()


if __name__ == '__main__':
    rawApp().run()
