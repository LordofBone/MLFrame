from datetime import datetime

from functions.inky_display import display_inky
from functions.neural_transfer import perform_neural_transfer


class BuildDisplay:
    def __init__(self, show_image):
        self.show_image = show_image

        self.now = datetime.now()

        self.dt_string = self.now.strftime("%d-%m-%Y_%H-%M-%S")

    def run_neural_transfer(self):
        perform_neural_transfer(self.dt_string, self.show_image)

    def display_to_ink(self):
        display_inky(self.dt_string)

    def display_random_to_ink(self):
        display_inky(file_time=self.dt_string, random_existing=True)
