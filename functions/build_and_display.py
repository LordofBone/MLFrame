from datetime import datetime

from functions.inky_display import display_inky
from functions.neural_transfer import perform_neural_transfer


# this is all within a class so that the datetime and show image parameters can be kept the same within image
# generation runs
class BuildDisplay:
    def __init__(self, show_image):
        self.show_image = show_image

        self.now = datetime.now()

        self.dt_string = self.now.strftime("%d-%m-%Y_%H-%M-%S")

    def run_neural_transfer(self):
        """
        This is the main function that runs the neural transfer
        :return:
        """
        perform_neural_transfer(self.dt_string, self.show_image)

    def display_to_ink(self):
        """
        This function displays the image to the inky display
        :return:
        """
        display_inky(self.dt_string)

    def display_random_to_ink(self):
        """
        This function displays a random image to the inky display
        :return:
        """
        display_inky(file_time=self.dt_string, random_existing=True)
