from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import math


class BoxLayoutDemo(App):
    def build(self):
        Window.size = (300, 150)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('miles_to_km_layout.kv')
        return self.root

    def handle_convert(self, value):
        """ handle calculation, output result to label widget """
        try:
            result = float(value) * 1.60934
            self.root.ids.output_value.text = "{:0.2f} kilometers".format(result)
        except ValueError:
            self.show_valid_number_error()

    def handle_increment(self, increment_value):
        input_value = self.root.ids.input_value.text
        try:
            if input_value.strip() == "":
                input_value = 0
            new_value = float(input_value) + increment_value
            self.root.ids.input_value.text = str(new_value)
            self.handle_convert(str(new_value))
        except ValueError:
            self.show_valid_number_error()

    def show_valid_number_error(self):
        self.root.ids.output_value.text = "Please enter valid miles to convert"


BoxLayoutDemo().run()