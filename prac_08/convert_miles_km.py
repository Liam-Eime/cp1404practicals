"""
CP1404 | Liam Eime | convert miles to kilometers exercise
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class ConvertMilesKmApp(App):
    """Convert Miles to Kilometers through a GUI"""
    kilometers = StringProperty()

    def build(self):
        """Build GUI"""
        self.title = "Converting Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_press(self, value):
        """Perform conversion on inputted miles to output equivalent kilometers"""
        miles = self.convert_string_to_number(value)
        self.kilometers = str(miles * CONVERSION_FACTOR)

    def handle_increment(self, value, delta):
        """Increment miles input"""
        miles = self.convert_string_to_number(value) + delta
        self.root.ids.input_number.text = str(miles)

    def convert_string_to_number(self, string):
        """Convert string to number"""
        try:
            number = float(string)
        except ValueError:
            number = 0.0
        return number


ConvertMilesKmApp().run()
