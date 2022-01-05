import os
import random
from pathlib import Path


# this is as a class to ensure that the base image path can always be accessed and added to to find images from the
# sub-folders
class FileHandler:
    def __init__(self):
        # folders under images are: input, style, output
        self.image_path = Path(__file__).parent / "../images"

    def get_random_file(self, folder="output"):
        d = f"{self.image_path}/{folder}"

        random_pot = []

        for path in os.listdir(d):
            file_path = os.path.join(d, path)
            random_pot.append(file_path)

        random_file = random.choice(random_pot)

        return random_file

    def get_specific_file(self, file_name, folder="output"):
        specific_file = f"{self.image_path}/{folder}/{file_name}"

        return specific_file


FileHandlerInstance = FileHandler()
