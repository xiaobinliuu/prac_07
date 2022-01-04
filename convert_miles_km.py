from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometersApp(App):

    def build(self):
        Window.size = (400, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, number):

        try:
            result = float(number) * 1.6093
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0"

    def handle_increment(self, number, different):

        up_down = float(number) + different
        self.root.ids.input_number.text = str(up_down)
        result = float(number) * 1.609344
        self.root.ids.output_label.text = str(result)


ConvertMilesToKilometersApp().run()
