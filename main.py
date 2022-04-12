from kivy.app import App
from kivy.lang.builder import Builder

"""
Подключаем графический интерфейс программы
"""
kv_file = Builder.load_string(open('app_ui.kv', encoding='utf8').read())


class MyApp(App):
    def build(self):
        return kv_file


if __name__ == "__main__":
    MyApp().run()
