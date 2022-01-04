from kivy.app import App
from kivy.lang import Builder


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.student_to_nickname = [["Jack", "Jackie"], ["Jim", "Jimmy"], ["Clark", "Clarky"]]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.display_information()

        return self.root

    def display_information(self):
        self.root.ids.output_label.text = "{} nickname is {}".format(self.student_to_nickname[0][0],
                                                                     self.student_to_nickname[0][1])
        self.root.ids.output_label_2.text = "{} nickname is {}".format(self.student_to_nickname[1][0],
                                                                       self.student_to_nickname[1][1])
        self.root.ids.output_label_3.text = "{} nickname is {}".format(self.student_to_nickname[2][0],
                                                                       self.student_to_nickname[2][1])


DynamicLabels().run()
